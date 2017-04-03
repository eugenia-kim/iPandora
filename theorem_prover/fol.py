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

    def visitFormula(self, ctx:folParser.FormulaContext):
        children = self.visitChildren(ctx)
        if ctx.VARIABLE() is None:
            return children
        elif ctx.FORALL():
            return "ForAll(" + ctx.VARIABLE().getText()[1:] + ", " + children + ")"
        else:
            return "Exists(" + ctx.VARIABLE().getText()[1:] + ", " + children + ")"

    def visitNegation(self, ctx:folParser.NegationContext):
        if ctx.NOT() is None:
            return self.visitChildren(ctx)
        else:
            children = self.visitChildren(ctx)
            return "Not(" + children + ")"

    def visitPredicate(self, ctx:folParser.PredicateContext):
        children = self.visitChildren(ctx)
        if children:
            return ctx.PREPOSITION().getText() + children
        else:
            return ctx.PREPOSITION().getText()

    def visitPredicateTuple(self, ctx:folParser.PredicateTupleContext):
        tuple_list = map((lambda t: self.visitTerm(t)), ctx.term())
        return "(" + self.__list_to_string(tuple_list) + ")"

    def visitTerm(self, ctx:folParser.TermContext):
        # TODO: function case
        return ctx.VARIABLE().getText()[1:]

    def visitIntermediate(self, ctx:folParser.IntermediateContext):
        return self.visit(ctx.condition())

    def visitImplication(self, ctx:folParser.ImplicationContext):
        if not ctx.IMPLIES():
            return self.visitChildren(ctx)
        else:
            disjunction_list = map((lambda d: self.visitDisjunction(d)), ctx.disjunction())
            return reduce((lambda a, b: "Implies(" + a + ", " + b + ")"), disjunction_list)

    def visitDisjunction(self, ctx:folParser.DisjunctionContext):
        print("visiting Disjunction!!!")
        if not ctx.OR():
            print("without OR")
            children = self.visitChildren(ctx)
            print(children)
            return children
        else:
            print("OR")
            conjunction_list = map((lambda c: self.visitConjunction(c)), ctx.conjunction())
            print(self.__list_to_string(conjunction_list))
            return "Or(" + self.__list_to_string(conjunction_list) + ")"

    def visitConjunction(self, ctx:folParser.ConjunctionContext):
        if not ctx.AND():
            return self.visitChildren(ctx)
        else:
            negation_list = map((lambda n: self.visitNegation(n)), ctx.negation())
            return "And(" + self.__list_to_string(negation_list) + ")"

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
