# Generated from fol.g4 by ANTLR 4.6
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\20")
        buf.write("r\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\7\4\'\n\4")
        buf.write("\f\4\16\4*\13\4\3\5\3\5\3\6\3\6\5\6\60\n\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\7\7\67\n\7\f\7\16\7:\13\7\3\b\3\b\3\b\7\b?\n")
        buf.write("\b\f\b\16\bB\13\b\3\t\5\tE\n\t\3\t\3\t\3\t\3\t\3\t\5\t")
        buf.write("L\n\t\3\n\3\n\3\n\5\nQ\n\n\3\13\3\13\3\13\3\13\7\13W\n")
        buf.write("\13\f\13\16\13Z\13\13\3\13\3\13\3\f\3\f\5\f`\n\f\3\r\3")
        buf.write("\r\3\r\5\re\n\r\3\16\3\16\3\16\3\16\7\16k\n\16\f\16\16")
        buf.write("\16n\13\16\3\16\3\16\3\16\2\2\17\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\2\5\3\2\r\16\3\2\b\t\3\2\n\13o\2\34\3\2\2")
        buf.write("\2\4 \3\2\2\2\6#\3\2\2\2\b+\3\2\2\2\n/\3\2\2\2\f\63\3")
        buf.write("\2\2\2\16;\3\2\2\2\20D\3\2\2\2\22P\3\2\2\2\24R\3\2\2\2")
        buf.write("\26_\3\2\2\2\30d\3\2\2\2\32f\3\2\2\2\34\35\5\4\3\2\35")
        buf.write("\36\5\6\4\2\36\37\7\2\2\3\37\3\3\2\2\2 !\7\r\2\2!\"\5")
        buf.write("\b\5\2\"\5\3\2\2\2#(\t\2\2\2$%\7\17\2\2%\'\t\2\2\2&$\3")
        buf.write("\2\2\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2\2)\7\3\2\2\2*(\3\2")
        buf.write("\2\2+,\5\n\6\2,\t\3\2\2\2-.\t\3\2\2.\60\7\n\2\2/-\3\2")
        buf.write("\2\2/\60\3\2\2\2\60\61\3\2\2\2\61\62\5\f\7\2\62\13\3\2")
        buf.write("\2\2\638\5\16\b\2\64\65\7\6\2\2\65\67\5\16\b\2\66\64\3")
        buf.write("\2\2\2\67:\3\2\2\28\66\3\2\2\289\3\2\2\29\r\3\2\2\2:8")
        buf.write("\3\2\2\2;@\5\20\t\2<=\7\5\2\2=?\5\20\t\2><\3\2\2\2?B\3")
        buf.write("\2\2\2@>\3\2\2\2@A\3\2\2\2A\17\3\2\2\2B@\3\2\2\2CE\7\7")
        buf.write("\2\2DC\3\2\2\2DE\3\2\2\2EK\3\2\2\2FL\5\22\n\2GH\7\3\2")
        buf.write("\2HI\5\n\6\2IJ\7\4\2\2JL\3\2\2\2KF\3\2\2\2KG\3\2\2\2L")
        buf.write("\21\3\2\2\2MN\7\f\2\2NQ\5\24\13\2OQ\7\f\2\2PM\3\2\2\2")
        buf.write("PO\3\2\2\2Q\23\3\2\2\2RS\7\3\2\2SX\5\26\f\2TU\7\17\2\2")
        buf.write("UW\5\26\f\2VT\3\2\2\2WZ\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y[")
        buf.write("\3\2\2\2ZX\3\2\2\2[\\\7\4\2\2\\\25\3\2\2\2]`\5\30\r\2")
        buf.write("^`\7\n\2\2_]\3\2\2\2_^\3\2\2\2`\27\3\2\2\2ab\7\13\2\2")
        buf.write("be\5\32\16\2ce\7\13\2\2da\3\2\2\2dc\3\2\2\2e\31\3\2\2")
        buf.write("\2fg\7\3\2\2gl\t\4\2\2hi\7\17\2\2ik\t\4\2\2jh\3\2\2\2")
        buf.write("kn\3\2\2\2lj\3\2\2\2lm\3\2\2\2mo\3\2\2\2nl\3\2\2\2op\7")
        buf.write("\4\2\2p\33\3\2\2\2\r(/8@DKPX_dl")
        return buf.getvalue()


class folParser ( Parser ):

    grammarFileName = "fol.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'&'", "'|'", "'!'", "'Forall'", 
                     "'Exists'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "','" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "AND", "OR", "NOT", 
                      "FORALL", "EXISTS", "VARIABLE", "CONSTANT", "PREPOSITION", 
                      "LINE", "CASE", "SEP", "WS" ]

    RULE_step = 0
    RULE_intermediate = 1
    RULE_justification = 2
    RULE_condition = 3
    RULE_formula = 4
    RULE_disjunction = 5
    RULE_conjunction = 6
    RULE_negation = 7
    RULE_predicate = 8
    RULE_predicateTuple = 9
    RULE_term = 10
    RULE_function = 11
    RULE_functionTuple = 12

    ruleNames =  [ "step", "intermediate", "justification", "condition", 
                   "formula", "disjunction", "conjunction", "negation", 
                   "predicate", "predicateTuple", "term", "function", "functionTuple" ]

    EOF = Token.EOF
    LPAREN=1
    RPAREN=2
    AND=3
    OR=4
    NOT=5
    FORALL=6
    EXISTS=7
    VARIABLE=8
    CONSTANT=9
    PREPOSITION=10
    LINE=11
    CASE=12
    SEP=13
    WS=14

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class StepContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def intermediate(self):
            return self.getTypedRuleContext(folParser.IntermediateContext,0)


        def justification(self):
            return self.getTypedRuleContext(folParser.JustificationContext,0)


        def EOF(self):
            return self.getToken(folParser.EOF, 0)

        def getRuleIndex(self):
            return folParser.RULE_step

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStep" ):
                listener.enterStep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStep" ):
                listener.exitStep(self)




    def step(self):

        localctx = folParser.StepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_step)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.intermediate()
            self.state = 27
            self.justification()
            self.state = 28
            self.match(folParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IntermediateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINE(self):
            return self.getToken(folParser.LINE, 0)

        def condition(self):
            return self.getTypedRuleContext(folParser.ConditionContext,0)


        def getRuleIndex(self):
            return folParser.RULE_intermediate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntermediate" ):
                listener.enterIntermediate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntermediate" ):
                listener.exitIntermediate(self)




    def intermediate(self):

        localctx = folParser.IntermediateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_intermediate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(folParser.LINE)
            self.state = 31
            self.condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class JustificationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINE(self, i:int=None):
            if i is None:
                return self.getTokens(folParser.LINE)
            else:
                return self.getToken(folParser.LINE, i)

        def CASE(self, i:int=None):
            if i is None:
                return self.getTokens(folParser.CASE)
            else:
                return self.getToken(folParser.CASE, i)

        def SEP(self, i:int=None):
            if i is None:
                return self.getTokens(folParser.SEP)
            else:
                return self.getToken(folParser.SEP, i)

        def getRuleIndex(self):
            return folParser.RULE_justification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJustification" ):
                listener.enterJustification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJustification" ):
                listener.exitJustification(self)




    def justification(self):

        localctx = folParser.JustificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_justification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            _la = self._input.LA(1)
            if not(_la==folParser.LINE or _la==folParser.CASE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==folParser.SEP:
                self.state = 34
                self.match(folParser.SEP)
                self.state = 35
                _la = self._input.LA(1)
                if not(_la==folParser.LINE or _la==folParser.CASE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formula(self):
            return self.getTypedRuleContext(folParser.FormulaContext,0)


        def getRuleIndex(self):
            return folParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = folParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.formula()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def disjunction(self):
            return self.getTypedRuleContext(folParser.DisjunctionContext,0)


        def VARIABLE(self):
            return self.getToken(folParser.VARIABLE, 0)

        def FORALL(self):
            return self.getToken(folParser.FORALL, 0)

        def EXISTS(self):
            return self.getToken(folParser.EXISTS, 0)

        def getRuleIndex(self):
            return folParser.RULE_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormula" ):
                listener.enterFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormula" ):
                listener.exitFormula(self)




    def formula(self):

        localctx = folParser.FormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_formula)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==folParser.FORALL or _la==folParser.EXISTS:
                self.state = 43
                _la = self._input.LA(1)
                if not(_la==folParser.FORALL or _la==folParser.EXISTS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 44
                self.match(folParser.VARIABLE)


            self.state = 47
            self.disjunction()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DisjunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conjunction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(folParser.ConjunctionContext)
            else:
                return self.getTypedRuleContext(folParser.ConjunctionContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(folParser.OR)
            else:
                return self.getToken(folParser.OR, i)

        def getRuleIndex(self):
            return folParser.RULE_disjunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisjunction" ):
                listener.enterDisjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisjunction" ):
                listener.exitDisjunction(self)




    def disjunction(self):

        localctx = folParser.DisjunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_disjunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.conjunction()
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==folParser.OR:
                self.state = 50
                self.match(folParser.OR)
                self.state = 51
                self.conjunction()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConjunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def negation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(folParser.NegationContext)
            else:
                return self.getTypedRuleContext(folParser.NegationContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(folParser.AND)
            else:
                return self.getToken(folParser.AND, i)

        def getRuleIndex(self):
            return folParser.RULE_conjunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjunction" ):
                listener.enterConjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjunction" ):
                listener.exitConjunction(self)




    def conjunction(self):

        localctx = folParser.ConjunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_conjunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.negation()
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==folParser.AND:
                self.state = 58
                self.match(folParser.AND)
                self.state = 59
                self.negation()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NegationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predicate(self):
            return self.getTypedRuleContext(folParser.PredicateContext,0)


        def LPAREN(self):
            return self.getToken(folParser.LPAREN, 0)

        def formula(self):
            return self.getTypedRuleContext(folParser.FormulaContext,0)


        def RPAREN(self):
            return self.getToken(folParser.RPAREN, 0)

        def NOT(self):
            return self.getToken(folParser.NOT, 0)

        def getRuleIndex(self):
            return folParser.RULE_negation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegation" ):
                listener.enterNegation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegation" ):
                listener.exitNegation(self)




    def negation(self):

        localctx = folParser.NegationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_negation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==folParser.NOT:
                self.state = 65
                self.match(folParser.NOT)


            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [folParser.PREPOSITION]:
                self.state = 68
                self.predicate()
                pass
            elif token in [folParser.LPAREN]:
                self.state = 69
                self.match(folParser.LPAREN)
                self.state = 70
                self.formula()
                self.state = 71
                self.match(folParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PredicateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREPOSITION(self):
            return self.getToken(folParser.PREPOSITION, 0)

        def predicateTuple(self):
            return self.getTypedRuleContext(folParser.PredicateTupleContext,0)


        def getRuleIndex(self):
            return folParser.RULE_predicate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicate" ):
                listener.enterPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicate" ):
                listener.exitPredicate(self)




    def predicate(self):

        localctx = folParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_predicate)
        try:
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.match(folParser.PREPOSITION)
                self.state = 76
                self.predicateTuple()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.match(folParser.PREPOSITION)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PredicateTupleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(folParser.LPAREN, 0)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(folParser.TermContext)
            else:
                return self.getTypedRuleContext(folParser.TermContext,i)


        def RPAREN(self):
            return self.getToken(folParser.RPAREN, 0)

        def getRuleIndex(self):
            return folParser.RULE_predicateTuple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicateTuple" ):
                listener.enterPredicateTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicateTuple" ):
                listener.exitPredicateTuple(self)




    def predicateTuple(self):

        localctx = folParser.PredicateTupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_predicateTuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(folParser.LPAREN)
            self.state = 81
            self.term()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==folParser.SEP:
                self.state = 82
                self.match(folParser.SEP)
                self.state = 83
                self.term()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self.match(folParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(folParser.FunctionContext,0)


        def VARIABLE(self):
            return self.getToken(folParser.VARIABLE, 0)

        def getRuleIndex(self):
            return folParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = folParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_term)
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [folParser.CONSTANT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.function()
                pass
            elif token in [folParser.VARIABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.match(folParser.VARIABLE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTANT(self):
            return self.getToken(folParser.CONSTANT, 0)

        def functionTuple(self):
            return self.getTypedRuleContext(folParser.FunctionTupleContext,0)


        def getRuleIndex(self):
            return folParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = folParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_function)
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.match(folParser.CONSTANT)
                self.state = 96
                self.functionTuple()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.match(folParser.CONSTANT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionTupleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(folParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(folParser.RPAREN, 0)

        def CONSTANT(self, i:int=None):
            if i is None:
                return self.getTokens(folParser.CONSTANT)
            else:
                return self.getToken(folParser.CONSTANT, i)

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(folParser.VARIABLE)
            else:
                return self.getToken(folParser.VARIABLE, i)

        def getRuleIndex(self):
            return folParser.RULE_functionTuple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionTuple" ):
                listener.enterFunctionTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionTuple" ):
                listener.exitFunctionTuple(self)




    def functionTuple(self):

        localctx = folParser.FunctionTupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_functionTuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(folParser.LPAREN)
            self.state = 101
            _la = self._input.LA(1)
            if not(_la==folParser.VARIABLE or _la==folParser.CONSTANT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==folParser.SEP:
                self.state = 102
                self.match(folParser.SEP)
                self.state = 103
                _la = self._input.LA(1)
                if not(_la==folParser.VARIABLE or _la==folParser.CONSTANT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 109
            self.match(folParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





