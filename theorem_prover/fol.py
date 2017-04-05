import sys
from antlr4 import *
from folLexer import folLexer
from folParser import folParser
#from folListener import folListener
from folVisitor import folVisitor
from functools import *

class folPrinter(folVisitor):
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
        if ctx.NOT() is None:
            print("without !")
            return self.visitChildren(ctx)
        else:
            print("with !")
            children = self.visitChildren(ctx)
            return "Not(" + children + ")"

    def visitPredicate(self, ctx: folParser.PredicateContext):
        children = self.visitChildren(ctx)
        if children:
            return ctx.PREPOSITION().getText() + children
        else:
            return ctx.PREPOSITION().getText()

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
            disjunctionList = map((lambda d: self.visit(d)), ctx.disjunction())
            return reduce((lambda a, b: "Implies(" + a + ", " + b + ")"), disjunctionList)

    def visitDisjunction(self, ctx: folParser.DisjunctionContext):
        print("Disjunction")
        if not ctx.OR():
            print("no |")
            return self.visit(ctx.conjunction(0))
        else:
            print("yes |")
            conjunctionList = map((lambda c: self.visit(c)), ctx.conjunction())
            return "Or(" + reduce((lambda a, b: a + ", " + b), conjunctionList) + ")"

    def visitConjunction(self, ctx: folParser.ConjunctionContext):
        print("Conjunction")
        if not ctx.AND():
            print("no &")
            return self.visit(ctx.negation(0))
        else:
            print("yes &")
            negationList = map((lambda n: self.visit(n)), ctx.negation())
            return "And(" + reduce((lambda a, b: a + ", " + b), negationList) + ")"

    def __list_to_string(self, list):
        return ', '.join(map(str, list))

def main(argv):
    input = FileStream(argv[1])
    lexer = folLexer(input)
    stream = CommonTokenStream(lexer)
    parser = folParser(stream)

    tree = parser.step()
    printer = folPrinter()
    print(printer.visit(tree))

if __name__ == '__main__':
    main(sys.argv)
