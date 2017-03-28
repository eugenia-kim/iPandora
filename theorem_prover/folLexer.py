# Generated from fol.g4 by ANTLR 4.6
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\16")
        buf.write("Z\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\5\n:\n\n\3\n\7\n=\n\n\f\n\16\n@\13\n\3\13\5")
        buf.write("\13C\n\13\3\13\7\13F\n\13\f\13\16\13I\13\13\3\f\3\f\7")
        buf.write("\fM\n\f\f\f\16\fP\13\f\3\r\3\r\3\16\6\16U\n\16\r\16\16")
        buf.write("\16V\3\16\3\16\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\2\33\16\3\2\5\4\2\62;c|\6\2\62;")
        buf.write("C\\aac|\5\2\13\f\17\17\"\"\\\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5\37\3\2\2\2\7!\3\2\2\2")
        buf.write("\t#\3\2\2\2\13%\3\2\2\2\r\'\3\2\2\2\17)\3\2\2\2\21\60")
        buf.write("\3\2\2\2\23\67\3\2\2\2\25B\3\2\2\2\27J\3\2\2\2\31Q\3\2")
        buf.write("\2\2\33T\3\2\2\2\35\36\7.\2\2\36\4\3\2\2\2\37 \7*\2\2")
        buf.write(" \6\3\2\2\2!\"\7+\2\2\"\b\3\2\2\2#$\7(\2\2$\n\3\2\2\2")
        buf.write("%&\7~\2\2&\f\3\2\2\2\'(\7#\2\2(\16\3\2\2\2)*\7H\2\2*+")
        buf.write("\7q\2\2+,\7t\2\2,-\7c\2\2-.\7n\2\2./\7n\2\2/\20\3\2\2")
        buf.write("\2\60\61\7G\2\2\61\62\7z\2\2\62\63\7k\2\2\63\64\7u\2\2")
        buf.write("\64\65\7v\2\2\65\66\7u\2\2\66\22\3\2\2\2\679\7A\2\28:")
        buf.write("\t\2\2\298\3\2\2\2:>\3\2\2\2;=\5\31\r\2<;\3\2\2\2=@\3")
        buf.write("\2\2\2><\3\2\2\2>?\3\2\2\2?\24\3\2\2\2@>\3\2\2\2AC\t\2")
        buf.write("\2\2BA\3\2\2\2CG\3\2\2\2DF\5\31\r\2ED\3\2\2\2FI\3\2\2")
        buf.write("\2GE\3\2\2\2GH\3\2\2\2H\26\3\2\2\2IG\3\2\2\2JN\4C\\\2")
        buf.write("KM\5\31\r\2LK\3\2\2\2MP\3\2\2\2NL\3\2\2\2NO\3\2\2\2O\30")
        buf.write("\3\2\2\2PN\3\2\2\2QR\t\3\2\2R\32\3\2\2\2SU\t\4\2\2TS\3")
        buf.write("\2\2\2UV\3\2\2\2VT\3\2\2\2VW\3\2\2\2WX\3\2\2\2XY\b\16")
        buf.write("\2\2Y\34\3\2\2\2\t\29>BGNV\3\b\2\2")
        return buf.getvalue()


class folLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    LPAREN = 2
    RPAREN = 3
    AND = 4
    OR = 5
    NOT = 6
    FORALL = 7
    EXISTS = 8
    VARIABLE = 9
    CONSTANT = 10
    PREPOSITION = 11
    WS = 12

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'('", "')'", "'&'", "'|'", "'!'", "'Forall'", "'Exists'" ]

    symbolicNames = [ "<INVALID>",
            "LPAREN", "RPAREN", "AND", "OR", "NOT", "FORALL", "EXISTS", 
            "VARIABLE", "CONSTANT", "PREPOSITION", "WS" ]

    ruleNames = [ "T__0", "LPAREN", "RPAREN", "AND", "OR", "NOT", "FORALL", 
                  "EXISTS", "VARIABLE", "CONSTANT", "PREPOSITION", "CHARACTER", 
                  "WS" ]

    grammarFileName = "fol.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


