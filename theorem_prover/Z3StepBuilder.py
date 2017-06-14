import argparse
from antlr4 import *
from folLexer import folLexer
from folParser import folParser
from folVisitor import folVisitor
from functools import *
from z3 import *
from Z3TypeBuilder import Z3TypeBuilder

from error.folSyntaxErrorListener import folSyntaxErrorListener


class Z3StepBuilder(folVisitor):

    def __init__(self, param_map = None, predicate_map = None, quantifier = dict()):

        # proposition_map = [proposition_name, z3 Bool]
        self.proposition_map = dict()

        # Z3 Type Builder which has predicate_map and param_map
        # self.type_builder = type_builder

        self.param_map = param_map

        self.predicate_map = predicate_map

        # var_map = [term_name, z3 sort] (bounded)
        self.var_map = dict()

        # constant_map = [term_name, z3 sort] (unbounded)
        self.constant_map = dict()

        self.__first_token = True

        self.quantifier = quantifier
        self.quantifier['exist'] = False
        self.quantifier['forall'] = False

    # Visit a parse tree produced by folParser#step.
    def visitStep(self, ctx: folParser.StepContext):
        return self.visit(ctx.formula())

    def visitFormula(self, ctx: folParser.FormulaContext):
        '''
             need to check the term is not in the var_map before. (var name should be different for the good practice in the inner scope from the outer one)
             set the term to unknown
             and when visiting predicate, you encounter first x, so you check the map
             AFTER I visit the implication.            
             DFS so I need to remove the var after retrieving
        '''
        if ctx.TRUE():
            return True
        elif ctx.FALSE():
            return False

        if ctx.VARIABLE():
            term = self.var_map.get(ctx.VARIABLE().getText()[1:])
            if term:
                # TODO: throw an error (bad practice to have the same bounded variable name in between levels of scopes
                raise Exception("Bad practice to have the same bounded variable name in between levels of scope: " + ctx.VARIABLE.getText()[1:])
            else:
                self.var_map[ctx.VARIABLE().getText()[1:]] = unknown

        children = self.visit(ctx.implication())

        if ctx.FORALL():
            term = self.var_map.get(ctx.VARIABLE().getText()[1:])
            self.var_map.pop(ctx.VARIABLE().getText()[1:])
            if self.__first_token:
                self.quantifier['forall'] = True
            self.__first_token = False
            return ForAll(term, children)
            # return "ForAll(" + ctx.VARIABLE().getText()[1:] + ", " + children + ")"
        elif ctx.EXISTS():
            term = self.var_map.get(ctx.VARIABLE().getText()[1:])
            self.var_map.pop(ctx.VARIABLE().getText()[1:])

            if self.__first_token:
                self.quantifier['exist'] = True
            self.__first_token = False
            return Exists(term, children)
            #return "Exists(" + ctx.VARIABLE().getText()[1:] + ", " + children + ")"
        else:
            return children

    def visitImplication(self, ctx: folParser.ImplicationContext):
        print("Implication")
        if not ctx.IMPLIES():
            print("no ->")
            return self.visit(ctx.disjunction(0))
        else:
            print("yes ->")
            disjunction_list = map((lambda d: self.visit(d)), ctx.disjunction())
            #return reduce((lambda a, b: "Implies(" + a + ", " + b + ")"), disjunction_list)
            return reduce((lambda a, b: Implies(a, b)), disjunction_list)

    def visitDisjunction(self, ctx: folParser.DisjunctionContext):
        print("Disjunction")
        if not ctx.OR():
            print("no |")
            return self.visit(ctx.conjunction(0))
        else:
            print("yes |")
            conjunction_list = map((lambda c: self.visit(c)), ctx.conjunction())
            #return "Or(" + reduce((lambda a, b: a + ", " + b), conjunction_list) + ")"
            return Or(*conjunction_list)

    def visitConjunction(self, ctx: folParser.ConjunctionContext):
        print("Conjunction")
        if not ctx.AND():
            print("no &")
            return self.visit(ctx.negation(0))
        else:
            print("yes &")
            negation_list = list(map((lambda n: self.visit(n)), ctx.negation()))
            #return "And(" + reduce((lambda a, b: a + ", " + b), negation_list) + ")"
            return And(*negation_list)

    def visitNegation(self, ctx: folParser.NegationContext):
        print("Negation")
        first_token = self.__first_token
        children = None
        if ctx.formula():
            children = self.visit(ctx.formula())
        else:
            children = self.visit(ctx.predicate())
        if ctx.NOT() is None:
            return children
        else:
            if first_token and (self.quantifier.get('exist') or self.quantifier.get('forall')):
                self.quantifier['exist'] = not self.quantifier.get('exist')
                self.quantifier['forall'] = not self.quantifier.get('forall')

            # return "Not(" + children + ")"
            return Not(children)

    def visitPredicate(self, ctx: folParser.PredicateContext):
        if ctx.predicateTuple():
            '''
                Green: _dragon -> _Bool
                Forall ?x Green(?x)
                tuple = [x]
                param_type = [_dragonZ3]
                predicate = Function('Green', _dragonZ3, BoolSort())
                z3_consts = [Const(x, _dragonZ3)]
            '''
            tuple = self.visit(ctx.predicateTuple())
            # Predicate Tuple type

            # get z3 parameter types
            param_type = self.param_map.get(ctx.PREPOSITION().getText())

            # get z3 predicate function
            predicate = self.predicate_map.get(ctx.PREPOSITION().getText())

            # get z3 model
            z3_consts = list(map((lambda t: Const(t[0], t[1])), zip(tuple, param_type)))

            # add z3 params to var_map. If it's in the var_map, it's a bounded variable. If not, it's an error.
            print(list(zip(tuple, z3_consts)))
            for name, param in zip(tuple, z3_consts):
                self.__add_var_map(name, param)

            return predicate(*z3_consts)
            # return ctx.PREPOSITION().getText() + children
        else:
            # simple predicate Bool type
            proposition = self.proposition_map.get(ctx.PREPOSITION().getText())
            if proposition is None:
                proposition = Bool(ctx.PREPOSITION().getText())
                self.proposition_map[ctx.PREPOSITION().getText()] = proposition
            return proposition
            #return ctx.PREPOSITION().getText()
            #return Bool(ctx.PREPOSITION().getText())

    def visitPredicateTuple(self, ctx: folParser.PredicateTupleContext):
        tuple_list = list(map((lambda t: self.visit(t)), ctx.term()))
        return tuple_list
        #return "(" + reduce((lambda a, b: a + ", " +  b), tuple_list) + ")"

    def visitTerm(self, ctx: folParser.TermContext):
        if ctx.VARIABLE():
            var_name = ctx.VARIABLE().getText()[1:]
            if self.var_map.get(var_name) is None:
                raise Exception("No variable declared: " + var_name)
            return var_name
        else:
            return self.visit(ctx.function())

    def visitFunction(self, ctx:folParser.FunctionContext):
        # TODO: functionTuple case
        constant = self.constant_map.get(ctx.CONSTANT().getText(), None)
        if constant is None:
            self.constant_map[ctx.CONSTANT().getText()] = unknown
        return ctx.CONSTANT().getText()

    def __add_var_map(self, name, z3):
        var = self.var_map.get(name, None)
        const = self.constant_map.get(name, None)
        if var is not None and const is not None:
            # Forall ?x (Friend(?x, x))
            del self.var_map[name]
            del self.constant_map[name]
            raise Exception("Bounded variable and unbounded constant cannot have the same name: " + name)
        if var is unknown:
            print("Var is in the map: " + name)
            self.var_map[name] = z3
        elif const is unknown:
            print("Constant is in the map: " + name)
            self.constant_map[name] = z3
            pass
        '''
        This seems like it will be dealt by Z3 Exception
         elif var is not None and var != z3:
            # {Green: _dragon, Friend: _human x _human. Forall ?x Green(?x) & (Forall ?y Friend(?x, ?y)) }
            raise "Type Error.. expected Type of " + name +  ": " + str(z3) + ", Found: " + str(var)
        '''



    def visitInput(self, step):
        input = InputStream(step)
        lexer = folLexer(input)
        stream = CommonTokenStream(lexer)
        parser = folParser(stream)
        errorListener = folSyntaxErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(errorListener)

        # Generate Parse tree and check for syntax errors
        tree = parser.step()
        if not errorListener.isGood():
            return False, None

        z3 = self.visit(tree)
        return True, z3

    def visitInputArray(self, array):
        z3 = []
        for i in array:
            input = InputStream(i)
            lexer = folLexer(input)
            stream = CommonTokenStream(lexer)
            parser = folParser(stream)
            tree = parser.step()

            z3.append(self.visit(tree))
        return z3


    def visitInputFile(self, file):
        lexer = folLexer(file)
        stream = CommonTokenStream(lexer)
        parser = folParser(stream)
        errorListener = folSyntaxErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(errorListener)

        tree = parser.step()
        if not errorListener.isGood():
            print("HI")
            return None
        return self.visit(tree)

def get_args():
    parser = argparse.ArgumentParser(
        description='Script builds z3 command from given proof steps and optional type declarations'
    )

    parser.add_argument(
        '-d', '--declaration', type=str, help='Declaration file path', required=False
    )

    parser.add_argument(
        '-s', '--step', type=str, help='Step file path', required=True
    )

    return parser.parse_args()

def main(argv):

    args = get_args()
    param_map = dict()
    predicate_map = dict()

    type_builder = Z3TypeBuilder(param_map, predicate_map)

    if args.declaration:
        type_input = FileStream(args.declaration)
        type_builder.visitInputFile(type_input)

    step_input = FileStream(args.step)
    step_builder = Z3StepBuilder(param_map, predicate_map)
    print(step_builder.visitInputFile(step_input))

if __name__ == '__main__':
    main(sys.argv)
