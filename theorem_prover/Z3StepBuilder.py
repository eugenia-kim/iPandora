import sys
from antlr4 import *
from folLexer import folLexer
from folParser import folParser
#from fol_listener import fol_listener
from folVisitor import folVisitor
from functools import *
from z3 import *

class Z3StepBuilder(folVisitor):

    def __init__(self):
        self.proposition_map = dict()

    # Visit a parse tree produced by folParser#step.
    def visitStep(self, ctx: folParser.StepContext):
        return self.visit(ctx.intermediate())

    def visitFormula(self, ctx: folParser.FormulaContext):
        children = self.visit(ctx.implication())
        if ctx.VARIABLE() is None:
            return children
        elif ctx.FORALL():
            return "ForAll(" + ctx.VARIABLE().getText()[1:] + ", " + children + ")"
        else:
            return "Exists(" + ctx.VARIABLE().getText()[1:] + ", " + children + ")"

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
        children = self.visitChildren(ctx)
        if children:
            # Predicate Tuple type
            return ctx.PREPOSITION().getText() + children
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
        tuple_list = map((lambda t: self.visit(t)), ctx.term())
        return "(" + reduce((lambda a, b: a + ", " +  b), tuple_list) + ")"

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

    def __list_to_string(self, list):
        return ', '.join(map(str, list))

def main(argv):
    input = FileStream(argv[1])
    lexer = folLexer(input)
    stream = CommonTokenStream(lexer)
    parser = folParser(stream)

    tree = parser.step()
    printer = Z3StepBuilder()
    print(str(printer.visit(tree)))

if __name__ == '__main__':
    main(sys.argv)
