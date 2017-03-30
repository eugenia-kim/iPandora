import sys
from antlr4 import *
from folLexer import folLexer
from folParser import folParser
#from folListener import folListener
from folVisitor import folVisitor

class folPrinter(folVisitor):

    # Visit a parse tree produced by folParser#step.
    def visitStep(self, ctx: folParser.StepContext):
        print("hi")
        return self.visitChildren(ctx)

def main(argv):
    input = FileStream(argv[1])
    lexer = folLexer(input)
    stream = CommonTokenStream(lexer)
    parser = folParser(stream)

    tree = parser.step()
    printer = folPrinter()
    printer.visit(tree)

if __name__ == '__main__':
    main(sys.argv)
