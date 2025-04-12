# Generated from Simple.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("V\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16")
        buf.write("\3\16\3\17\6\17E\n\17\r\17\16\17F\3\20\3\20\7\20K\n\20")
        buf.write("\f\20\16\20N\13\20\3\21\6\21Q\n\21\r\21\16\21R\3\21\3")
        buf.write("\21\2\2\22\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22\3\2\6\3\2\62;\5\2")
        buf.write("C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2X\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\3#\3\2\2\2\5)\3\2\2\2\7")
        buf.write("+\3\2\2\2\t-\3\2\2\2\13\61\3\2\2\2\r\63\3\2\2\2\17\65")
        buf.write("\3\2\2\2\21\67\3\2\2\2\239\3\2\2\2\25;\3\2\2\2\27=\3\2")
        buf.write("\2\2\31?\3\2\2\2\33A\3\2\2\2\35D\3\2\2\2\37H\3\2\2\2!")
        buf.write("P\3\2\2\2#$\7e\2\2$%\7n\2\2%&\7c\2\2&\'\7u\2\2\'(\7u\2")
        buf.write("\2(\4\3\2\2\2)*\7}\2\2*\6\3\2\2\2+,\7\177\2\2,\b\3\2\2")
        buf.write("\2-.\7k\2\2./\7p\2\2/\60\7v\2\2\60\n\3\2\2\2\61\62\7=")
        buf.write("\2\2\62\f\3\2\2\2\63\64\7*\2\2\64\16\3\2\2\2\65\66\7+")
        buf.write("\2\2\66\20\3\2\2\2\678\7.\2\28\22\3\2\2\29:\7?\2\2:\24")
        buf.write("\3\2\2\2;<\7,\2\2<\26\3\2\2\2=>\7\61\2\2>\30\3\2\2\2?")
        buf.write("@\7-\2\2@\32\3\2\2\2AB\7/\2\2B\34\3\2\2\2CE\t\2\2\2DC")
        buf.write("\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2\2G\36\3\2\2\2HL\t")
        buf.write("\3\2\2IK\t\4\2\2JI\3\2\2\2KN\3\2\2\2LJ\3\2\2\2LM\3\2\2")
        buf.write("\2M \3\2\2\2NL\3\2\2\2OQ\t\5\2\2PO\3\2\2\2QR\3\2\2\2R")
        buf.write("P\3\2\2\2RS\3\2\2\2ST\3\2\2\2TU\b\21\2\2U\"\3\2\2\2\6")
        buf.write("\2FLR\3\b\2\2")
        return buf.getvalue()


class SimpleLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    INT = 14
    ID = 15
    WS = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'class'", "'{'", "'}'", "'int'", "';'", "'('", "')'", "','", 
            "'='", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "ID", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "INT", 
                  "ID", "WS" ]

    grammarFileName = "Simple.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


