import sys
from antlr4 import *
from folLexer import folLexer
from folParser import folParser
from folListener import folListener

class folPrinter(folListener):
    def enterStep(self, ctx):
        print("hi")

def main(argv):
    input = FileStream(argv[1])
    lexer = folLexer(input)
    stream = CommonTokenStream(lexer)
    parser = folParser(stream)

    tree = parser.step()
    printer = folPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    print("done")

if __name__ == '__main__':
    main(sys.argv)
