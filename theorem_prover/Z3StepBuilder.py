import sys
import argparse
from antlr4 import *
from folLexer import folLexer
from folParser import folParser
from folVisitor import folVisitor
from functools import *
from z3 import *
from Z3TypeBuilder import Z3TypeBuilder

class Z3StepBuilder(folVisitor):

    def __init__(self, type_builder):
        # proposition_map = [proposition_name, z3 Bool]
        self.proposition_map = dict()

        # Z3 Type Builder which has predicate_map and param_map
        self.type_builder = type_builder

        # term_map = [term_name, z3 sort]
        self.term_map = dict()

    # Visit a parse tree produced by folParser#step.
    def visitStep(self, ctx: folParser.StepContext):
        return self.visit(ctx.intermediate())

    def visitFormula(self, ctx: folParser.FormulaContext):
        children = self.visit(ctx.implication())
        if ctx.VARIABLE() is None:
            return children
        elif ctx.FORALL():
            term = self.term_map.get(ctx.VARIABLE().getText()[1:])
            return ForAll(term, children)
            # return "ForAll(" + ctx.VARIABLE().getText()[1:] + ", " + children + ")"
        else:
            term = self.term_map.get(ctx.VARIABLE().getText()[1:])
            return Exists(term, children)
            #return "Exists(" + ctx.VARIABLE().getText()[1:] + ", " + children + ")"

    def visitNegation(self, ctx: folParser.NegationContext):
        print("Negation")
        children = None
        if ctx.formula():
            children = self.visit(ctx.formula())
        else:
            children = self.visit(ctx.predicate())
        if ctx.NOT() is None:
            return children
        else:
            # return "Not(" + children + ")"
            return Not(children)

    def visitPredicate(self, ctx: folParser.PredicateContext):
        # TODO: change this to visit(ctx.predicateTuple())
        children = self.visitChildren(ctx)
        if children:
            # Predicate Tuple type

            # get z3 parameter types
            param_type = self.type_builder.param_map.get(ctx.PREPOSITION().getText())

            # get z3 predicate function
            predicate = self.type_builder.predicate_map.get(ctx.PREPOSITION().getText())

            # get z3 constants
            z3_consts = list(map((lambda tuple: Const(tuple[0], tuple[1])), zip(children, param_type)))

            # add z3 params to term_map
            print(list(zip(children, z3_consts)))
            for name, param in zip(children, z3_consts):
                self.__add_term_map(name, param)

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
        # TODO: function case
        return ctx.VARIABLE().getText()[1:]

    def visitIntermediate(self, ctx: folParser.IntermediateContext):
        print("Intermediate")
        return self.visit(ctx.condition())

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
            negation_list = map((lambda n: self.visit(n)), ctx.negation())
            #return "And(" + reduce((lambda a, b: a + ", " + b), negation_list) + ")"
            return And(*negation_list)

    def __add_term_map(self, name, z3):
       if self.term_map.get(name) is None:
           self.term_map[name] = z3

    def visitInputFile(self, file):
        lexer = folLexer(file)
        stream = CommonTokenStream(lexer)
        parser = folParser(stream)

        tree = parser.step()
        print(str(self.visit(tree)))

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

    type_builder = Z3TypeBuilder()

    if args.declaration:
        type_input = FileStream(args.declaration)
        type_builder.visitInputFile(type_input)

    step_input = FileStream(args.step)
    step_builder = Z3StepBuilder(type_builder)
    step_builder.visitInputFile(step_input)

if __name__ == '__main__':
    main(sys.argv)
