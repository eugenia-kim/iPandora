import sys
from antlr4 import *
from folTypeLexer import folTypeLexer
from folTypeParser import folTypeParser
from folTypeVisitor import folTypeVisitor
from functools import *
from z3 import *

class Z3TypeBuilder(folTypeVisitor):

    def __init__(self):

        '''
            this is only for predicates not propositions as it is not necessary to declare propositions' types
        '''
        # from user's type to z3 type sort
        self.type_map = dict()

        # from user's predicate type to z3's function type
        self.predicate_map = dict()

    # Visit a parse tree produced by folTypeParser#init.
    def visitInit(self, ctx: folTypeParser.InitContext):
        print("visitInit")
        self.visitChildren(ctx)
        #declaration_list = list(map((lambda d: self.visit(d), print("done")), ctx.declaration()))
        #TODO: figure out why below line is working but not the line above
        self.visit(ctx.declaration(0))
        for k, v in self.predicate_map.items():
            print("key and val")
            print(k, v)

    # Visit a parse tree produced by folTypeParser#declaration.
    def visitDeclaration(self, ctx: folTypeParser.DeclarationContext):
        print("visitDeclaration")
        declaration = self.predicate_map.get(ctx.PREPOSITION().getText())
        if declaration is None:
            children = self.visit(ctx.predicateType())
            children.append(BoolSort())
            print(children)
            declaration = Function(ctx.PREPOSITION().getText(), *children)
            self.predicate_map[ctx.PREPOSITION().getText()] = declaration

        return declaration

    # Visit a parse tree produced by folTypeParser#predicateType.
    def visitPredicateType(self, ctx: folTypeParser.PredicateTypeContext):
        print("visitPredicateType")
        return list(map((lambda s: self.visit(s)), ctx.sort()))

    # Visit a parse tree produced by folTypeParser#sort.
    def visitSort(self, ctx: folTypeParser.SortContext):
        print("visitSort")
        if ctx.INT():
            return IntSort()
        elif ctx.BOOL():
            return BoolSort()
        else:
            type = self.type_map.get(ctx.TYPE().getText()[1:])
            if type is None:
                type = DeclareSort(ctx.TYPE().getText()[1:])
                self.type_map[ctx.TYPE().getText()[1:]] = type
            return type

def main(argv):
    input = FileStream(argv[1])
    lexer = folTypeLexer(input)
    stream = CommonTokenStream(lexer)
    parser = folTypeParser(stream)

    tree = parser.init()
    printer = Z3TypeBuilder()
    printer.visit(tree)

if __name__ == '__main__':
    main(sys.argv)
