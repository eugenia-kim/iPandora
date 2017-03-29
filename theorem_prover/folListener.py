# Generated from fol.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .folParser import folParser
else:
    from folParser import folParser

# This class defines a complete listener for a parse tree produced by folParser.
class folListener(ParseTreeListener):

    # Enter a parse tree produced by folParser#step.
    def enterStep(self, ctx:folParser.StepContext):
        pass

    # Exit a parse tree produced by folParser#step.
    def exitStep(self, ctx:folParser.StepContext):
        pass


    # Enter a parse tree produced by folParser#intermediate.
    def enterIntermediate(self, ctx:folParser.IntermediateContext):
        pass

    # Exit a parse tree produced by folParser#intermediate.
    def exitIntermediate(self, ctx:folParser.IntermediateContext):
        pass


    # Enter a parse tree produced by folParser#justification.
    def enterJustification(self, ctx:folParser.JustificationContext):
        pass

    # Exit a parse tree produced by folParser#justification.
    def exitJustification(self, ctx:folParser.JustificationContext):
        pass


    # Enter a parse tree produced by folParser#condition.
    def enterCondition(self, ctx:folParser.ConditionContext):
        pass

    # Exit a parse tree produced by folParser#condition.
    def exitCondition(self, ctx:folParser.ConditionContext):
        pass


    # Enter a parse tree produced by folParser#formula.
    def enterFormula(self, ctx:folParser.FormulaContext):
        pass

    # Exit a parse tree produced by folParser#formula.
    def exitFormula(self, ctx:folParser.FormulaContext):
        pass


    # Enter a parse tree produced by folParser#disjunction.
    def enterDisjunction(self, ctx:folParser.DisjunctionContext):
        pass

    # Exit a parse tree produced by folParser#disjunction.
    def exitDisjunction(self, ctx:folParser.DisjunctionContext):
        pass


    # Enter a parse tree produced by folParser#conjunction.
    def enterConjunction(self, ctx:folParser.ConjunctionContext):
        pass

    # Exit a parse tree produced by folParser#conjunction.
    def exitConjunction(self, ctx:folParser.ConjunctionContext):
        pass


    # Enter a parse tree produced by folParser#negation.
    def enterNegation(self, ctx:folParser.NegationContext):
        pass

    # Exit a parse tree produced by folParser#negation.
    def exitNegation(self, ctx:folParser.NegationContext):
        pass


    # Enter a parse tree produced by folParser#predicate.
    def enterPredicate(self, ctx:folParser.PredicateContext):
        pass

    # Exit a parse tree produced by folParser#predicate.
    def exitPredicate(self, ctx:folParser.PredicateContext):
        pass


    # Enter a parse tree produced by folParser#predicateTuple.
    def enterPredicateTuple(self, ctx:folParser.PredicateTupleContext):
        pass

    # Exit a parse tree produced by folParser#predicateTuple.
    def exitPredicateTuple(self, ctx:folParser.PredicateTupleContext):
        pass


    # Enter a parse tree produced by folParser#term.
    def enterTerm(self, ctx:folParser.TermContext):
        pass

    # Exit a parse tree produced by folParser#term.
    def exitTerm(self, ctx:folParser.TermContext):
        pass


    # Enter a parse tree produced by folParser#function.
    def enterFunction(self, ctx:folParser.FunctionContext):
        pass

    # Exit a parse tree produced by folParser#function.
    def exitFunction(self, ctx:folParser.FunctionContext):
        pass


    # Enter a parse tree produced by folParser#functionTuple.
    def enterFunctionTuple(self, ctx:folParser.FunctionTupleContext):
        pass

    # Exit a parse tree produced by folParser#functionTuple.
    def exitFunctionTuple(self, ctx:folParser.FunctionTupleContext):
        pass


