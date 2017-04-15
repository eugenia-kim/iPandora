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

        self.given = None
        self.toShow = None

        # step_map = [line number. z3 formula]
        self.step_map = dict()

        # proposition_map = [proposition_name, z3 Bool]
        self.proposition_map = dict()

        # Z3 Type Builder which has predicate_map and param_map
        self.type_builder = type_builder

        # term_map = [term_name, z3 sort]
        self.term_map = dict()

    # Visit a parse tree produced by folParser#step.
    def visitStep(self, ctx: folParser.StepContext):
        justification = self.visit(ctx.justification())
        condition = self.visit(ctx.intermediate())

        if justification == "given":
            self.given = condition
        elif justification == "toShow":
            self.toShow = condition
        else:
            print("LINE LIST!!!!")
        # TODO: elif justification == "ass": and line_list
        return condition

    def visitIntermediate(self, ctx: folParser.IntermediateContext):
        print("Intermediate")
        condition = self.visit(ctx.condition())
        self.step_map[ctx.LINE().getText()[1:]] = condition
        return condition

    def visitJustification(self, ctx: folParser.JustificationContext):
        if ctx.line():
            line_list = list(map((lambda l: self.visit(l)), ctx.line()))
            return line_list
        elif ctx.GIVEN():
            return ctx.GIVEN().getText()[1:]
        elif ctx.TOSHOW():
            return ctx.TOSHOW().getText()[1:]
        elif ctx.ASS():
            return ctx.ASS().getText()[1:]

    def visitLine(self, ctx: folParser.LineContext):
        # TODO: add CASE once debugged in fol.g4
        return ctx.LINE().getText()[1:]

    def visitCondition(self, ctx: folParser.ConditionContext):
        return self.visit(ctx.formula())

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
            param_type = self.type_builder.param_map.get(ctx.PREPOSITION().getText())

            # get z3 predicate function
            predicate = self.type_builder.predicate_map.get(ctx.PREPOSITION().getText())

            # get z3 constants
            z3_consts = list(map((lambda tuple: Const(tuple[0], tuple[1])), zip(tuple, param_type)))

            # add z3 params to term_map
            print(list(zip(tuple, z3_consts)))
            for name, param in zip(tuple, z3_consts):
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
