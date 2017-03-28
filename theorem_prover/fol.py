import sys
from antlr4 import *
from folLexer import folLexer
from folParser import folParser
from folListener import folListener

def main(argv):
    input = FileStream(argv[1])
    lexer = folLexer(input)
    stream = CommonTokenStream(lexer)
    parser = folParser(stream)
    tree = parser.condition()
    printer = folListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    if __name__ == '__main__':
        main(sys.argv)
