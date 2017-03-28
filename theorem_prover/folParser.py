# Generated from fol.g4 by ANTLR 4.6
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\16")
        buf.write("^\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\3\3\3\5\3")
        buf.write("\34\n\3\3\3\3\3\3\4\3\4\3\4\7\4#\n\4\f\4\16\4&\13\4\3")
        buf.write("\5\3\5\3\5\7\5+\n\5\f\5\16\5.\13\5\3\6\5\6\61\n\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\5\68\n\6\3\7\3\7\3\7\5\7=\n\7\3\b\3\b")
        buf.write("\3\b\3\b\7\bC\n\b\f\b\16\bF\13\b\3\b\3\b\3\t\3\t\5\tL")
        buf.write("\n\t\3\n\3\n\3\n\5\nQ\n\n\3\13\3\13\3\13\3\13\7\13W\n")
        buf.write("\13\f\13\16\13Z\13\13\3\13\3\13\3\13\2\2\f\2\4\6\b\n\f")
        buf.write("\16\20\22\24\2\4\3\2\t\n\3\2\13\f]\2\26\3\2\2\2\4\33\3")
        buf.write("\2\2\2\6\37\3\2\2\2\b\'\3\2\2\2\n\60\3\2\2\2\f<\3\2\2")
        buf.write("\2\16>\3\2\2\2\20K\3\2\2\2\22P\3\2\2\2\24R\3\2\2\2\26")
        buf.write("\27\5\4\3\2\27\30\7\2\2\3\30\3\3\2\2\2\31\32\t\2\2\2\32")
        buf.write("\34\7\13\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34\35\3\2\2\2")
        buf.write("\35\36\5\6\4\2\36\5\3\2\2\2\37$\5\b\5\2 !\7\7\2\2!#\5")
        buf.write("\b\5\2\" \3\2\2\2#&\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%\7\3")
        buf.write("\2\2\2&$\3\2\2\2\',\5\n\6\2()\7\6\2\2)+\5\n\6\2*(\3\2")
        buf.write("\2\2+.\3\2\2\2,*\3\2\2\2,-\3\2\2\2-\t\3\2\2\2.,\3\2\2")
        buf.write("\2/\61\7\b\2\2\60/\3\2\2\2\60\61\3\2\2\2\61\67\3\2\2\2")
        buf.write("\628\5\f\7\2\63\64\7\4\2\2\64\65\5\4\3\2\65\66\7\5\2\2")
        buf.write("\668\3\2\2\2\67\62\3\2\2\2\67\63\3\2\2\28\13\3\2\2\29")
        buf.write(":\7\r\2\2:=\5\16\b\2;=\7\r\2\2<9\3\2\2\2<;\3\2\2\2=\r")
        buf.write("\3\2\2\2>?\7\4\2\2?D\5\20\t\2@A\7\3\2\2AC\5\20\t\2B@\3")
        buf.write("\2\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2EG\3\2\2\2FD\3\2\2")
        buf.write("\2GH\7\5\2\2H\17\3\2\2\2IL\5\22\n\2JL\7\13\2\2KI\3\2\2")
        buf.write("\2KJ\3\2\2\2L\21\3\2\2\2MN\7\f\2\2NQ\5\24\13\2OQ\7\f\2")
        buf.write("\2PM\3\2\2\2PO\3\2\2\2Q\23\3\2\2\2RS\7\4\2\2SX\t\3\2\2")
        buf.write("TU\7\3\2\2UW\t\3\2\2VT\3\2\2\2WZ\3\2\2\2XV\3\2\2\2XY\3")
        buf.write("\2\2\2Y[\3\2\2\2ZX\3\2\2\2[\\\7\5\2\2\\\25\3\2\2\2\f\33")
        buf.write("$,\60\67<DKPX")
        return buf.getvalue()


class folParser ( Parser ):

    grammarFileName = "fol.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'('", "')'", "'&'", "'|'", "'!'", 
                     "'Forall'", "'Exists'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "LPAREN", "RPAREN", "AND", 
                      "OR", "NOT", "FORALL", "EXISTS", "VARIABLE", "CONSTANT", 
                      "PREPOSITION", "WS" ]

    RULE_condition = 0
    RULE_formula = 1
    RULE_disjunction = 2
    RULE_conjunction = 3
    RULE_negation = 4
    RULE_predicate = 5
    RULE_predicateTuple = 6
    RULE_term = 7
    RULE_function = 8
    RULE_functionTuple = 9

    ruleNames =  [ "condition", "formula", "disjunction", "conjunction", 
                   "negation", "predicate", "predicateTuple", "term", "function", 
                   "functionTuple" ]

    EOF = Token.EOF
    T__0=1
    LPAREN=2
    RPAREN=3
    AND=4
    OR=5
    NOT=6
    FORALL=7
    EXISTS=8
    VARIABLE=9
    CONSTANT=10
    PREPOSITION=11
    WS=12

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formula(self):
            return self.getTypedRuleContext(folParser.FormulaContext,0)


        def EOF(self):
            return self.getToken(folParser.EOF, 0)

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
        self.enterRule(localctx, 0, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.formula()
            self.state = 21
            self.match(folParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_formula)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==folParser.FORALL or _la==folParser.EXISTS:
                self.state = 23
                _la = self._input.LA(1)
                if not(_la==folParser.FORALL or _la==folParser.EXISTS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 24
                self.match(folParser.VARIABLE)


            self.state = 27
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
        self.enterRule(localctx, 4, self.RULE_disjunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.conjunction()
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==folParser.OR:
                self.state = 30
                self.match(folParser.OR)
                self.state = 31
                self.conjunction()
                self.state = 36
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
        self.enterRule(localctx, 6, self.RULE_conjunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.negation()
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==folParser.AND:
                self.state = 38
                self.match(folParser.AND)
                self.state = 39
                self.negation()
                self.state = 44
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
        self.enterRule(localctx, 8, self.RULE_negation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==folParser.NOT:
                self.state = 45
                self.match(folParser.NOT)


            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [folParser.PREPOSITION]:
                self.state = 48
                self.predicate()
                pass
            elif token in [folParser.LPAREN]:
                self.state = 49
                self.match(folParser.LPAREN)
                self.state = 50
                self.formula()
                self.state = 51
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
        self.enterRule(localctx, 10, self.RULE_predicate)
        try:
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.match(folParser.PREPOSITION)
                self.state = 56
                self.predicateTuple()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
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
        self.enterRule(localctx, 12, self.RULE_predicateTuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(folParser.LPAREN)
            self.state = 61
            self.term()
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==folParser.T__0:
                self.state = 62
                self.match(folParser.T__0)
                self.state = 63
                self.term()
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 69
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
        self.enterRule(localctx, 14, self.RULE_term)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [folParser.CONSTANT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.function()
                pass
            elif token in [folParser.VARIABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
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
        self.enterRule(localctx, 16, self.RULE_function)
        try:
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.match(folParser.CONSTANT)
                self.state = 76
                self.functionTuple()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
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
        self.enterRule(localctx, 18, self.RULE_functionTuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(folParser.LPAREN)
            self.state = 81
            _la = self._input.LA(1)
            if not(_la==folParser.VARIABLE or _la==folParser.CONSTANT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==folParser.T__0:
                self.state = 82
                self.match(folParser.T__0)
                self.state = 83
                _la = self._input.LA(1)
                if not(_la==folParser.VARIABLE or _la==folParser.CONSTANT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
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





