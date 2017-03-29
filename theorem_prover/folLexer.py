# Generated from fol.g4 by ANTLR 4.6
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\20")
        buf.write("j\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\5\t<\n\t\3\t\7\t?\n\t\f\t\16\t")
        buf.write("B\13\t\3\n\5\nE\n\n\3\n\7\nH\n\n\f\n\16\nK\13\n\3\13\3")
        buf.write("\13\7\13O\n\13\f\13\16\13R\13\13\3\f\3\f\6\fV\n\f\r\f")
        buf.write("\16\fW\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\20")
        buf.write("\6\20e\n\20\r\20\16\20f\3\20\3\20\2\2\21\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\2")
        buf.write("\37\20\3\2\5\4\2\62;c|\6\2\62;C\\aac|\5\2\13\f\17\17\"")
        buf.write("\"m\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3")
        buf.write("\2\2\2\2\37\3\2\2\2\3!\3\2\2\2\5#\3\2\2\2\7%\3\2\2\2\t")
        buf.write("\'\3\2\2\2\13)\3\2\2\2\r+\3\2\2\2\17\62\3\2\2\2\219\3")
        buf.write("\2\2\2\23D\3\2\2\2\25L\3\2\2\2\27S\3\2\2\2\31Y\3\2\2\2")
        buf.write("\33_\3\2\2\2\35a\3\2\2\2\37d\3\2\2\2!\"\7*\2\2\"\4\3\2")
        buf.write("\2\2#$\7+\2\2$\6\3\2\2\2%&\7(\2\2&\b\3\2\2\2\'(\7~\2\2")
        buf.write("(\n\3\2\2\2)*\7#\2\2*\f\3\2\2\2+,\7H\2\2,-\7q\2\2-.\7")
        buf.write("t\2\2./\7c\2\2/\60\7n\2\2\60\61\7n\2\2\61\16\3\2\2\2\62")
        buf.write("\63\7G\2\2\63\64\7z\2\2\64\65\7k\2\2\65\66\7u\2\2\66\67")
        buf.write("\7v\2\2\678\7u\2\28\20\3\2\2\29;\7A\2\2:<\t\2\2\2;:\3")
        buf.write("\2\2\2<@\3\2\2\2=?\5\35\17\2>=\3\2\2\2?B\3\2\2\2@>\3\2")
        buf.write("\2\2@A\3\2\2\2A\22\3\2\2\2B@\3\2\2\2CE\t\2\2\2DC\3\2\2")
        buf.write("\2EI\3\2\2\2FH\5\35\17\2GF\3\2\2\2HK\3\2\2\2IG\3\2\2\2")
        buf.write("IJ\3\2\2\2J\24\3\2\2\2KI\3\2\2\2LP\4C\\\2MO\5\35\17\2")
        buf.write("NM\3\2\2\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2Q\26\3\2\2\2R")
        buf.write("P\3\2\2\2SU\7\u0080\2\2TV\4\62;\2UT\3\2\2\2VW\3\2\2\2")
        buf.write("WU\3\2\2\2WX\3\2\2\2X\30\3\2\2\2YZ\5\3\2\2Z[\5\27\f\2")
        buf.write("[\\\5\33\16\2\\]\5\27\f\2]^\5\5\3\2^\32\3\2\2\2_`\7.\2")
        buf.write("\2`\34\3\2\2\2ab\t\3\2\2b\36\3\2\2\2ce\t\4\2\2dc\3\2\2")
        buf.write("\2ef\3\2\2\2fd\3\2\2\2fg\3\2\2\2gh\3\2\2\2hi\b\20\2\2")
        buf.write("i \3\2\2\2\n\2;@DIPWf\3\b\2\2")
        return buf.getvalue()


class folLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    LPAREN = 1
    RPAREN = 2
    AND = 3
    OR = 4
    NOT = 5
    FORALL = 6
    EXISTS = 7
    VARIABLE = 8
    CONSTANT = 9
    PREPOSITION = 10
    LINE = 11
    CASE = 12
    SEP = 13
    WS = 14

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'&'", "'|'", "'!'", "'Forall'", "'Exists'", "','" ]

    symbolicNames = [ "<INVALID>",
            "LPAREN", "RPAREN", "AND", "OR", "NOT", "FORALL", "EXISTS", 
            "VARIABLE", "CONSTANT", "PREPOSITION", "LINE", "CASE", "SEP", 
            "WS" ]

    ruleNames = [ "LPAREN", "RPAREN", "AND", "OR", "NOT", "FORALL", "EXISTS", 
                  "VARIABLE", "CONSTANT", "PREPOSITION", "LINE", "CASE", 
                  "SEP", "CHARACTER", "WS" ]

    grammarFileName = "fol.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


