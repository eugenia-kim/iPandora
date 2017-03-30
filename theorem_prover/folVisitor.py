# Generated from fol.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .folParser import folParser
else:
    from folParser import folParser

# This class defines a complete generic visitor for a parse tree produced by folParser.

class folVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by folParser#step.
    def visitStep(self, ctx:folParser.StepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by folParser#intermediate.
    def visitIntermediate(self, ctx:folParser.IntermediateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by folParser#justification.
    def visitJustification(self, ctx:folParser.JustificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by folParser#condition.
    def visitCondition(self, ctx:folParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by folParser#formula.
    def visitFormula(self, ctx:folParser.FormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by folParser#implication.
    def visitImplication(self, ctx:folParser.ImplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by folParser#disjunction.
    def visitDisjunction(self, ctx:folParser.DisjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by folParser#conjunction.
    def visitConjunction(self, ctx:folParser.ConjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by folParser#negation.
    def visitNegation(self, ctx:folParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by folParser#predicate.
    def visitPredicate(self, ctx:folParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by folParser#predicateTuple.
    def visitPredicateTuple(self, ctx:folParser.PredicateTupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by folParser#term.
    def visitTerm(self, ctx:folParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by folParser#function.
    def visitFunction(self, ctx:folParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by folParser#functionTuple.
    def visitFunctionTuple(self, ctx:folParser.FunctionTupleContext):
        return self.visitChildren(ctx)



del folParser