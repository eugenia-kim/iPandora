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

    def visitNegation(self, ctx:folParser.NegationContext):
        if ctx.NOT() is None:
            return self.visitChildren(ctx)
        else:
            children = self.visitChildren(ctx)
            return "Not(" + children + ")"

    def visitPredicate(self, ctx:folParser.PredicateContext):
        return ctx.PREPOSITION().getText()

    def visitIntermediate(self, ctx:folParser.IntermediateContext):
        return self.visit(ctx.condition())

    def visitImplication(self, ctx:folParser.ImplicationContext):
        disjunctionList = map((lambda d: self.visitDisjunction(d)), ctx.disjunction())
        return reduce((lambda a, b: "Implies(" + a + ", " + b + ")"), disjunctionList)


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
