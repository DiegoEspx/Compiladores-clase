# Generated from Simple.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("\\\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\6\2\20\n\2\r\2\16\2\21\3\3\3\3\3\3\3\3\6\3\30\n\3\r\3")
        buf.write("\16\3\31\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4%\n\4")
        buf.write("\3\4\3\4\3\4\7\4*\n\4\f\4\16\4-\13\4\3\4\5\4\60\n\4\3")
        buf.write("\5\3\5\3\5\7\5\65\n\5\f\5\16\58\13\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\5\6B\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\5\7O\n\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7W\n")
        buf.write("\7\f\7\16\7Z\13\7\3\7\2\3\f\b\2\4\6\b\n\f\2\4\3\2\f\r")
        buf.write("\3\2\16\17\2a\2\17\3\2\2\2\4\23\3\2\2\2\6/\3\2\2\2\b\61")
        buf.write("\3\2\2\2\nA\3\2\2\2\fN\3\2\2\2\16\20\5\4\3\2\17\16\3\2")
        buf.write("\2\2\20\21\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22\3\3")
        buf.write("\2\2\2\23\24\7\3\2\2\24\25\7\21\2\2\25\27\7\4\2\2\26\30")
        buf.write("\5\6\4\2\27\26\3\2\2\2\30\31\3\2\2\2\31\27\3\2\2\2\31")
        buf.write("\32\3\2\2\2\32\33\3\2\2\2\33\34\7\5\2\2\34\5\3\2\2\2\35")
        buf.write("\36\7\6\2\2\36\37\7\21\2\2\37\60\7\7\2\2 !\7\6\2\2!\"")
        buf.write("\7\21\2\2\"$\7\b\2\2#%\5\b\5\2$#\3\2\2\2$%\3\2\2\2%&\3")
        buf.write("\2\2\2&\'\7\t\2\2\'+\7\4\2\2(*\5\n\6\2)(\3\2\2\2*-\3\2")
        buf.write("\2\2+)\3\2\2\2+,\3\2\2\2,.\3\2\2\2-+\3\2\2\2.\60\7\5\2")
        buf.write("\2/\35\3\2\2\2/ \3\2\2\2\60\7\3\2\2\2\61\66\7\21\2\2\62")
        buf.write("\63\7\n\2\2\63\65\7\21\2\2\64\62\3\2\2\2\658\3\2\2\2\66")
        buf.write("\64\3\2\2\2\66\67\3\2\2\2\67\t\3\2\2\28\66\3\2\2\29:\5")
        buf.write("\f\7\2:;\7\7\2\2;B\3\2\2\2<=\7\21\2\2=>\7\13\2\2>?\5\f")
        buf.write("\7\2?@\7\7\2\2@B\3\2\2\2A9\3\2\2\2A<\3\2\2\2B\13\3\2\2")
        buf.write("\2CD\b\7\1\2DO\7\20\2\2EO\7\21\2\2FG\7\21\2\2GH\7\b\2")
        buf.write("\2HI\7\20\2\2IO\7\t\2\2JK\7\b\2\2KL\5\f\7\2LM\7\t\2\2")
        buf.write("MO\3\2\2\2NC\3\2\2\2NE\3\2\2\2NF\3\2\2\2NJ\3\2\2\2OX\3")
        buf.write("\2\2\2PQ\f\b\2\2QR\t\2\2\2RW\5\f\7\tST\f\7\2\2TU\t\3\2")
        buf.write("\2UW\5\f\7\bVP\3\2\2\2VS\3\2\2\2WZ\3\2\2\2XV\3\2\2\2X")
        buf.write("Y\3\2\2\2Y\r\3\2\2\2ZX\3\2\2\2\f\21\31$+/\66ANVX")
        return buf.getvalue()


class SimpleParser ( Parser ):

    grammarFileName = "Simple.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'{'", "'}'", "'int'", "';'", 
                     "'('", "')'", "','", "'='", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT", "ID", "WS" ]

    RULE_prog = 0
    RULE_classDef = 1
    RULE_member = 2
    RULE_paramList = 3
    RULE_stat = 4
    RULE_expr = 5

    ruleNames =  [ "prog", "classDef", "member", "paramList", "stat", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    INT=14
    ID=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleParser.ClassDefContext)
            else:
                return self.getTypedRuleContext(SimpleParser.ClassDefContext,i)


        def getRuleIndex(self):
            return SimpleParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = SimpleParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.classDef()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SimpleParser.T__0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleParser.ID, 0)

        def member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleParser.MemberContext)
            else:
                return self.getTypedRuleContext(SimpleParser.MemberContext,i)


        def getRuleIndex(self):
            return SimpleParser.RULE_classDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDef" ):
                listener.enterClassDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDef" ):
                listener.exitClassDef(self)




    def classDef(self):

        localctx = SimpleParser.ClassDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(SimpleParser.T__0)
            self.state = 18
            self.match(SimpleParser.ID)
            self.state = 19
            self.match(SimpleParser.T__1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.member()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SimpleParser.T__3):
                    break

            self.state = 25
            self.match(SimpleParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleParser.ID, 0)

        def paramList(self):
            return self.getTypedRuleContext(SimpleParser.ParamListContext,0)


        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleParser.StatContext)
            else:
                return self.getTypedRuleContext(SimpleParser.StatContext,i)


        def getRuleIndex(self):
            return SimpleParser.RULE_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMember" ):
                listener.enterMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMember" ):
                listener.exitMember(self)




    def member(self):

        localctx = SimpleParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_member)
        self._la = 0 # Token type
        try:
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(SimpleParser.T__3)
                self.state = 28
                self.match(SimpleParser.ID)
                self.state = 29
                self.match(SimpleParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.match(SimpleParser.T__3)
                self.state = 31
                self.match(SimpleParser.ID)
                self.state = 32
                self.match(SimpleParser.T__5)
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SimpleParser.ID:
                    self.state = 33
                    self.paramList()


                self.state = 36
                self.match(SimpleParser.T__6)
                self.state = 37
                self.match(SimpleParser.T__1)
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleParser.T__5) | (1 << SimpleParser.INT) | (1 << SimpleParser.ID))) != 0):
                    self.state = 38
                    self.stat()
                    self.state = 43
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 44
                self.match(SimpleParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleParser.ID)
            else:
                return self.getToken(SimpleParser.ID, i)

        def getRuleIndex(self):
            return SimpleParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)




    def paramList(self):

        localctx = SimpleParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(SimpleParser.ID)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SimpleParser.T__7:
                self.state = 48
                self.match(SimpleParser.T__7)
                self.state = 49
                self.match(SimpleParser.ID)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SimpleParser.ExprContext,0)


        def ID(self):
            return self.getToken(SimpleParser.ID, 0)

        def getRuleIndex(self):
            return SimpleParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)




    def stat(self):

        localctx = SimpleParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stat)
        try:
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.expr(0)
                self.state = 56
                self.match(SimpleParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.match(SimpleParser.ID)
                self.state = 59
                self.match(SimpleParser.T__8)
                self.state = 60
                self.expr(0)
                self.state = 61
                self.match(SimpleParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class CallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleParser.ID, 0)
        def INT(self):
            return self.getToken(SimpleParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SimpleParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(SimpleParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = SimpleParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 66
                self.match(SimpleParser.INT)
                pass

            elif la_ == 2:
                localctx = SimpleParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 67
                self.match(SimpleParser.ID)
                pass

            elif la_ == 3:
                localctx = SimpleParser.CallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 68
                self.match(SimpleParser.ID)
                self.state = 69
                self.match(SimpleParser.T__5)
                self.state = 70
                self.match(SimpleParser.INT)
                self.state = 71
                self.match(SimpleParser.T__6)
                pass

            elif la_ == 4:
                localctx = SimpleParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 72
                self.match(SimpleParser.T__5)
                self.state = 73
                self.expr(0)
                self.state = 74
                self.match(SimpleParser.T__6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 86
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 84
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = SimpleParser.MulDivContext(self, SimpleParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 78
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 79
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SimpleParser.T__9 or _la==SimpleParser.T__10):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 80
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = SimpleParser.AddSubContext(self, SimpleParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 81
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 82
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SimpleParser.T__11 or _la==SimpleParser.T__12):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 83
                        self.expr(6)
                        pass

             
                self.state = 88
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




