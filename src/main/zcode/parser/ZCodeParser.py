# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\63")
        buf.write("\u01ee\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0080\n\3\3\4")
        buf.write("\3\4\5\4\u0084\n\4\3\5\3\5\5\5\u0088\n\5\3\5\3\5\3\5\3")
        buf.write("\5\5\5\u008e\n\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u0096\n\5")
        buf.write("\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00a2\n\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\5\n\u00ae\n\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\5\13\u00b5\n\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\5\f\u00bc\n\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u00c7\n\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\5\21\u00d7")
        buf.write("\n\21\3\22\3\22\3\22\3\22\3\22\5\22\u00de\n\22\3\23\3")
        buf.write("\23\3\23\3\23\5\23\u00e4\n\23\3\24\3\24\5\24\u00e8\n\24")
        buf.write("\3\24\5\24\u00eb\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\26\3\26\3\26\3\26\5\26\u00f7\n\26\3\27\3\27\5\27\u00fb")
        buf.write("\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0105")
        buf.write("\n\30\3\31\3\31\5\31\u0109\n\31\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\5\32\u0112\n\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\5\33\u0119\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5")
        buf.write("\34\u0122\n\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \5 \u0137")
        buf.write("\n \3!\3!\3!\3!\5!\u013d\n!\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\5\"\u0146\n\"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3%\3%\5%\u015a\n%\3%\3%\3%\3%\3&\3&\3&\3&\3")
        buf.write("&\3&\5&\u0166\n&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3")
        buf.write("*\3*\3*\3+\3+\3+\3+\5+\u017a\n+\3,\3,\3,\3,\3,\5,\u0181")
        buf.write("\n,\3-\3-\3-\3-\3-\5-\u0188\n-\3.\3.\3.\3.\3.\5.\u018f")
        buf.write("\n.\3/\3/\3/\3/\3/\3/\7/\u0197\n/\f/\16/\u019a\13/\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\7\60\u01a2\n\60\f\60\16\60\u01a5")
        buf.write("\13\60\3\61\3\61\3\61\3\61\3\61\3\61\7\61\u01ad\n\61\f")
        buf.write("\61\16\61\u01b0\13\61\3\62\3\62\3\62\5\62\u01b5\n\62\3")
        buf.write("\63\3\63\3\63\5\63\u01ba\n\63\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\5\64\u01c3\n\64\3\65\3\65\3\65\3\65\3\66\3")
        buf.write("\66\3\67\3\67\5\67\u01cd\n\67\3\67\3\67\3\67\3\67\38\3")
        buf.write("8\38\38\38\39\39\39\39\39\3:\3:\3:\3:\3:\5:\u01e2\n:\3")
        buf.write(";\3;\3;\5;\u01e7\n;\3<\3<\3<\5<\u01ec\n<\3<\2\5\\^`=\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtv\2\b\3\2\3\5\3\2\6")
        buf.write("\7\3\2#$\3\2\24\25\3\2\26\30\5\2\31\32\34\37!!\2\u01e7")
        buf.write("\2x\3\2\2\2\4\177\3\2\2\2\6\u0083\3\2\2\2\b\u0095\3\2")
        buf.write("\2\2\n\u0097\3\2\2\2\f\u0099\3\2\2\2\16\u009b\3\2\2\2")
        buf.write("\20\u00a5\3\2\2\2\22\u00ad\3\2\2\2\24\u00b4\3\2\2\2\26")
        buf.write("\u00bb\3\2\2\2\30\u00bd\3\2\2\2\32\u00c6\3\2\2\2\34\u00c8")
        buf.write("\3\2\2\2\36\u00ce\3\2\2\2 \u00d6\3\2\2\2\"\u00dd\3\2\2")
        buf.write("\2$\u00df\3\2\2\2&\u00ea\3\2\2\2(\u00ec\3\2\2\2*\u00f6")
        buf.write("\3\2\2\2,\u00fa\3\2\2\2.\u0104\3\2\2\2\60\u0108\3\2\2")
        buf.write("\2\62\u0111\3\2\2\2\64\u0118\3\2\2\2\66\u011a\3\2\2\2")
        buf.write("8\u0123\3\2\2\2:\u012a\3\2\2\2<\u012e\3\2\2\2>\u0136\3")
        buf.write("\2\2\2@\u013c\3\2\2\2B\u013e\3\2\2\2D\u0147\3\2\2\2F\u014e")
        buf.write("\3\2\2\2H\u0159\3\2\2\2J\u0165\3\2\2\2L\u0167\3\2\2\2")
        buf.write("N\u016a\3\2\2\2P\u016d\3\2\2\2R\u0170\3\2\2\2T\u0179\3")
        buf.write("\2\2\2V\u0180\3\2\2\2X\u0187\3\2\2\2Z\u018e\3\2\2\2\\")
        buf.write("\u0190\3\2\2\2^\u019b\3\2\2\2`\u01a6\3\2\2\2b\u01b4\3")
        buf.write("\2\2\2d\u01b9\3\2\2\2f\u01c2\3\2\2\2h\u01c4\3\2\2\2j\u01c8")
        buf.write("\3\2\2\2l\u01cc\3\2\2\2n\u01d2\3\2\2\2p\u01d7\3\2\2\2")
        buf.write("r\u01e1\3\2\2\2t\u01e6\3\2\2\2v\u01eb\3\2\2\2xy\5\4\3")
        buf.write("\2yz\7\2\2\3z\3\3\2\2\2{|\5\6\4\2|}\5\4\3\2}\u0080\3\2")
        buf.write("\2\2~\u0080\5\6\4\2\177{\3\2\2\2\177~\3\2\2\2\u0080\5")
        buf.write("\3\2\2\2\u0081\u0084\5\b\5\2\u0082\u0084\5\34\17\2\u0083")
        buf.write("\u0081\3\2\2\2\u0083\u0082\3\2\2\2\u0084\7\3\2\2\2\u0085")
        buf.write("\u0088\5\n\6\2\u0086\u0088\7\7\2\2\u0087\u0085\3\2\2\2")
        buf.write("\u0087\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a\7")
        buf.write("\60\2\2\u008a\u0096\5t;\2\u008b\u008e\5\n\6\2\u008c\u008e")
        buf.write("\5\f\7\2\u008d\u008b\3\2\2\2\u008d\u008c\3\2\2\2\u008e")
        buf.write("\u008f\3\2\2\2\u008f\u0090\7\60\2\2\u0090\u0091\7\33\2")
        buf.write("\2\u0091\u0092\5X-\2\u0092\u0093\5t;\2\u0093\u0096\3\2")
        buf.write("\2\2\u0094\u0096\5\16\b\2\u0095\u0087\3\2\2\2\u0095\u008d")
        buf.write("\3\2\2\2\u0095\u0094\3\2\2\2\u0096\t\3\2\2\2\u0097\u0098")
        buf.write("\t\2\2\2\u0098\13\3\2\2\2\u0099\u009a\t\3\2\2\u009a\r")
        buf.write("\3\2\2\2\u009b\u009c\5\n\6\2\u009c\u009d\7\60\2\2\u009d")
        buf.write("\u00a1\5\20\t\2\u009e\u009f\7\33\2\2\u009f\u00a2\5\24")
        buf.write("\13\2\u00a0\u00a2\3\2\2\2\u00a1\u009e\3\2\2\2\u00a1\u00a0")
        buf.write("\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\5t;\2\u00a4\17")
        buf.write("\3\2\2\2\u00a5\u00a6\7\'\2\2\u00a6\u00a7\5\22\n\2\u00a7")
        buf.write("\u00a8\7(\2\2\u00a8\21\3\2\2\2\u00a9\u00aa\7,\2\2\u00aa")
        buf.write("\u00ab\7)\2\2\u00ab\u00ae\5\22\n\2\u00ac\u00ae\7,\2\2")
        buf.write("\u00ad\u00a9\3\2\2\2\u00ad\u00ac\3\2\2\2\u00ae\23\3\2")
        buf.write("\2\2\u00af\u00b5\5\30\r\2\u00b0\u00b1\7\'\2\2\u00b1\u00b2")
        buf.write("\5\26\f\2\u00b2\u00b3\7(\2\2\u00b3\u00b5\3\2\2\2\u00b4")
        buf.write("\u00af\3\2\2\2\u00b4\u00b0\3\2\2\2\u00b5\25\3\2\2\2\u00b6")
        buf.write("\u00b7\5\30\r\2\u00b7\u00b8\7)\2\2\u00b8\u00b9\5\26\f")
        buf.write("\2\u00b9\u00bc\3\2\2\2\u00ba\u00bc\5\30\r\2\u00bb\u00b6")
        buf.write("\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc\27\3\2\2\2\u00bd\u00be")
        buf.write("\7\'\2\2\u00be\u00bf\5\32\16\2\u00bf\u00c0\7(\2\2\u00c0")
        buf.write("\31\3\2\2\2\u00c1\u00c2\5X-\2\u00c2\u00c3\7)\2\2\u00c3")
        buf.write("\u00c4\5\32\16\2\u00c4\u00c7\3\2\2\2\u00c5\u00c7\5X-\2")
        buf.write("\u00c6\u00c1\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7\33\3\2")
        buf.write("\2\2\u00c8\u00c9\7\t\2\2\u00c9\u00ca\7\60\2\2\u00ca\u00cb")
        buf.write("\5\36\20\2\u00cb\u00cc\5v<\2\u00cc\u00cd\5&\24\2\u00cd")
        buf.write("\35\3\2\2\2\u00ce\u00cf\7%\2\2\u00cf\u00d0\5 \21\2\u00d0")
        buf.write("\u00d1\7&\2\2\u00d1\37\3\2\2\2\u00d2\u00d3\5$\23\2\u00d3")
        buf.write("\u00d4\5\"\22\2\u00d4\u00d7\3\2\2\2\u00d5\u00d7\3\2\2")
        buf.write("\2\u00d6\u00d2\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7!\3\2")
        buf.write("\2\2\u00d8\u00d9\7)\2\2\u00d9\u00da\5$\23\2\u00da\u00db")
        buf.write("\5\"\22\2\u00db\u00de\3\2\2\2\u00dc\u00de\3\2\2\2\u00dd")
        buf.write("\u00d8\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de#\3\2\2\2\u00df")
        buf.write("\u00e0\5\n\6\2\u00e0\u00e3\7\60\2\2\u00e1\u00e4\5\20\t")
        buf.write("\2\u00e2\u00e4\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e2")
        buf.write("\3\2\2\2\u00e4%\3\2\2\2\u00e5\u00e8\5(\25\2\u00e6\u00e8")
        buf.write("\5J&\2\u00e7\u00e5\3\2\2\2\u00e7\u00e6\3\2\2\2\u00e8\u00eb")
        buf.write("\3\2\2\2\u00e9\u00eb\5t;\2\u00ea\u00e7\3\2\2\2\u00ea\u00e9")
        buf.write("\3\2\2\2\u00eb\'\3\2\2\2\u00ec\u00ed\7\22\2\2\u00ed\u00ee")
        buf.write("\5t;\2\u00ee\u00ef\5*\26\2\u00ef\u00f0\7\23\2\2\u00f0")
        buf.write("\u00f1\5t;\2\u00f1)\3\2\2\2\u00f2\u00f3\5,\27\2\u00f3")
        buf.write("\u00f4\5*\26\2\u00f4\u00f7\3\2\2\2\u00f5\u00f7\3\2\2\2")
        buf.write("\u00f6\u00f2\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7+\3\2\2")
        buf.write("\2\u00f8\u00fb\5.\30\2\u00f9\u00fb\5\60\31\2\u00fa\u00f8")
        buf.write("\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb-\3\2\2\2\u00fc\u0105")
        buf.write("\5\b\5\2\u00fd\u0105\5H%\2\u00fe\u0105\5L\'\2\u00ff\u0105")
        buf.write("\5N(\2\u0100\u0105\5J&\2\u0101\u0105\5P)\2\u0102\u0105")
        buf.write("\5(\25\2\u0103\u0105\5F$\2\u0104\u00fc\3\2\2\2\u0104\u00fd")
        buf.write("\3\2\2\2\u0104\u00fe\3\2\2\2\u0104\u00ff\3\2\2\2\u0104")
        buf.write("\u0100\3\2\2\2\u0104\u0101\3\2\2\2\u0104\u0102\3\2\2\2")
        buf.write("\u0104\u0103\3\2\2\2\u0105/\3\2\2\2\u0106\u0109\5\62\32")
        buf.write("\2\u0107\u0109\5\64\33\2\u0108\u0106\3\2\2\2\u0108\u0107")
        buf.write("\3\2\2\2\u0109\61\3\2\2\2\u010a\u010b\5\66\34\2\u010b")
        buf.write("\u010c\5> \2\u010c\u0112\3\2\2\2\u010d\u010e\58\35\2\u010e")
        buf.write("\u010f\5@!\2\u010f\u0110\5:\36\2\u0110\u0112\3\2\2\2\u0111")
        buf.write("\u010a\3\2\2\2\u0111\u010d\3\2\2\2\u0112\63\3\2\2\2\u0113")
        buf.write("\u0119\5.\30\2\u0114\u0115\58\35\2\u0115\u0116\5@!\2\u0116")
        buf.write("\u0117\5<\37\2\u0117\u0119\3\2\2\2\u0118\u0113\3\2\2\2")
        buf.write("\u0118\u0114\3\2\2\2\u0119\65\3\2\2\2\u011a\u011b\7\17")
        buf.write("\2\2\u011b\u011c\7%\2\2\u011c\u011d\5X-\2\u011d\u011e")
        buf.write("\7&\2\2\u011e\u0121\5v<\2\u011f\u0122\5.\30\2\u0120\u0122")
        buf.write("\5\62\32\2\u0121\u011f\3\2\2\2\u0121\u0120\3\2\2\2\u0122")
        buf.write("\67\3\2\2\2\u0123\u0124\7\17\2\2\u0124\u0125\7%\2\2\u0125")
        buf.write("\u0126\5X-\2\u0126\u0127\7&\2\2\u0127\u0128\5v<\2\u0128")
        buf.write("\u0129\5\64\33\2\u01299\3\2\2\2\u012a\u012b\7\20\2\2\u012b")
        buf.write("\u012c\5v<\2\u012c\u012d\5\62\32\2\u012d;\3\2\2\2\u012e")
        buf.write("\u012f\7\20\2\2\u012f\u0130\5v<\2\u0130\u0131\5\64\33")
        buf.write("\2\u0131=\3\2\2\2\u0132\u0133\5B\"\2\u0133\u0134\5> \2")
        buf.write("\u0134\u0137\3\2\2\2\u0135\u0137\3\2\2\2\u0136\u0132\3")
        buf.write("\2\2\2\u0136\u0135\3\2\2\2\u0137?\3\2\2\2\u0138\u0139")
        buf.write("\5D#\2\u0139\u013a\5@!\2\u013a\u013d\3\2\2\2\u013b\u013d")
        buf.write("\3\2\2\2\u013c\u0138\3\2\2\2\u013c\u013b\3\2\2\2\u013d")
        buf.write("A\3\2\2\2\u013e\u013f\7\21\2\2\u013f\u0140\7%\2\2\u0140")
        buf.write("\u0141\5X-\2\u0141\u0142\7&\2\2\u0142\u0145\5v<\2\u0143")
        buf.write("\u0146\5.\30\2\u0144\u0146\5\62\32\2\u0145\u0143\3\2\2")
        buf.write("\2\u0145\u0144\3\2\2\2\u0146C\3\2\2\2\u0147\u0148\7\21")
        buf.write("\2\2\u0148\u0149\7%\2\2\u0149\u014a\5X-\2\u014a\u014b")
        buf.write("\7&\2\2\u014b\u014c\5v<\2\u014c\u014d\5\64\33\2\u014d")
        buf.write("E\3\2\2\2\u014e\u014f\7\n\2\2\u014f\u0150\7\60\2\2\u0150")
        buf.write("\u0151\7\13\2\2\u0151\u0152\5X-\2\u0152\u0153\7\f\2\2")
        buf.write("\u0153\u0154\5X-\2\u0154\u0155\5v<\2\u0155\u0156\5,\27")
        buf.write("\2\u0156G\3\2\2\2\u0157\u015a\7\60\2\2\u0158\u015a\5p")
        buf.write("9\2\u0159\u0157\3\2\2\2\u0159\u0158\3\2\2\2\u015a\u015b")
        buf.write("\3\2\2\2\u015b\u015c\7\33\2\2\u015c\u015d\5X-\2\u015d")
        buf.write("\u015e\5t;\2\u015eI\3\2\2\2\u015f\u0160\7\b\2\2\u0160")
        buf.write("\u0161\5X-\2\u0161\u0162\5t;\2\u0162\u0166\3\2\2\2\u0163")
        buf.write("\u0164\7\b\2\2\u0164\u0166\5t;\2\u0165\u015f\3\2\2\2\u0165")
        buf.write("\u0163\3\2\2\2\u0166K\3\2\2\2\u0167\u0168\7\r\2\2\u0168")
        buf.write("\u0169\5t;\2\u0169M\3\2\2\2\u016a\u016b\7\16\2\2\u016b")
        buf.write("\u016c\5t;\2\u016cO\3\2\2\2\u016d\u016e\5R*\2\u016e\u016f")
        buf.write("\5t;\2\u016fQ\3\2\2\2\u0170\u0171\7\60\2\2\u0171\u0172")
        buf.write("\7%\2\2\u0172\u0173\5T+\2\u0173\u0174\7&\2\2\u0174S\3")
        buf.write("\2\2\2\u0175\u0176\5X-\2\u0176\u0177\5V,\2\u0177\u017a")
        buf.write("\3\2\2\2\u0178\u017a\3\2\2\2\u0179\u0175\3\2\2\2\u0179")
        buf.write("\u0178\3\2\2\2\u017aU\3\2\2\2\u017b\u017c\7)\2\2\u017c")
        buf.write("\u017d\5X-\2\u017d\u017e\5V,\2\u017e\u0181\3\2\2\2\u017f")
        buf.write("\u0181\3\2\2\2\u0180\u017b\3\2\2\2\u0180\u017f\3\2\2\2")
        buf.write("\u0181W\3\2\2\2\u0182\u0183\5Z.\2\u0183\u0184\7 \2\2\u0184")
        buf.write("\u0185\5Z.\2\u0185\u0188\3\2\2\2\u0186\u0188\5Z.\2\u0187")
        buf.write("\u0182\3\2\2\2\u0187\u0186\3\2\2\2\u0188Y\3\2\2\2\u0189")
        buf.write("\u018a\5\\/\2\u018a\u018b\5j\66\2\u018b\u018c\5\\/\2\u018c")
        buf.write("\u018f\3\2\2\2\u018d\u018f\5\\/\2\u018e\u0189\3\2\2\2")
        buf.write("\u018e\u018d\3\2\2\2\u018f[\3\2\2\2\u0190\u0191\b/\1\2")
        buf.write("\u0191\u0192\5^\60\2\u0192\u0198\3\2\2\2\u0193\u0194\f")
        buf.write("\4\2\2\u0194\u0195\t\4\2\2\u0195\u0197\5^\60\2\u0196\u0193")
        buf.write("\3\2\2\2\u0197\u019a\3\2\2\2\u0198\u0196\3\2\2\2\u0198")
        buf.write("\u0199\3\2\2\2\u0199]\3\2\2\2\u019a\u0198\3\2\2\2\u019b")
        buf.write("\u019c\b\60\1\2\u019c\u019d\5`\61\2\u019d\u01a3\3\2\2")
        buf.write("\2\u019e\u019f\f\4\2\2\u019f\u01a0\t\5\2\2\u01a0\u01a2")
        buf.write("\5`\61\2\u01a1\u019e\3\2\2\2\u01a2\u01a5\3\2\2\2\u01a3")
        buf.write("\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4_\3\2\2\2\u01a5")
        buf.write("\u01a3\3\2\2\2\u01a6\u01a7\b\61\1\2\u01a7\u01a8\5b\62")
        buf.write("\2\u01a8\u01ae\3\2\2\2\u01a9\u01aa\f\4\2\2\u01aa\u01ab")
        buf.write("\t\6\2\2\u01ab\u01ad\5b\62\2\u01ac\u01a9\3\2\2\2\u01ad")
        buf.write("\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2")
        buf.write("\u01afa\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1\u01b2\7\"\2")
        buf.write("\2\u01b2\u01b5\5b\62\2\u01b3\u01b5\5d\63\2\u01b4\u01b1")
        buf.write("\3\2\2\2\u01b4\u01b3\3\2\2\2\u01b5c\3\2\2\2\u01b6\u01b7")
        buf.write("\7\25\2\2\u01b7\u01ba\5d\63\2\u01b8\u01ba\5f\64\2\u01b9")
        buf.write("\u01b6\3\2\2\2\u01b9\u01b8\3\2\2\2\u01bae\3\2\2\2\u01bb")
        buf.write("\u01c3\7,\2\2\u01bc\u01c3\7-\2\2\u01bd\u01c3\7.\2\2\u01be")
        buf.write("\u01c3\7\60\2\2\u01bf\u01c3\5l\67\2\u01c0\u01c3\5R*\2")
        buf.write("\u01c1\u01c3\5h\65\2\u01c2\u01bb\3\2\2\2\u01c2\u01bc\3")
        buf.write("\2\2\2\u01c2\u01bd\3\2\2\2\u01c2\u01be\3\2\2\2\u01c2\u01bf")
        buf.write("\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c1\3\2\2\2\u01c3")
        buf.write("g\3\2\2\2\u01c4\u01c5\7%\2\2\u01c5\u01c6\5X-\2\u01c6\u01c7")
        buf.write("\7&\2\2\u01c7i\3\2\2\2\u01c8\u01c9\t\7\2\2\u01c9k\3\2")
        buf.write("\2\2\u01ca\u01cd\7\60\2\2\u01cb\u01cd\5R*\2\u01cc\u01ca")
        buf.write("\3\2\2\2\u01cc\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce")
        buf.write("\u01cf\7\'\2\2\u01cf\u01d0\5r:\2\u01d0\u01d1\7(\2\2\u01d1")
        buf.write("m\3\2\2\2\u01d2\u01d3\5R*\2\u01d3\u01d4\7\'\2\2\u01d4")
        buf.write("\u01d5\5r:\2\u01d5\u01d6\7(\2\2\u01d6o\3\2\2\2\u01d7\u01d8")
        buf.write("\7\60\2\2\u01d8\u01d9\7\'\2\2\u01d9\u01da\5r:\2\u01da")
        buf.write("\u01db\7(\2\2\u01dbq\3\2\2\2\u01dc\u01dd\5X-\2\u01dd\u01de")
        buf.write("\7)\2\2\u01de\u01df\5r:\2\u01df\u01e2\3\2\2\2\u01e0\u01e2")
        buf.write("\5X-\2\u01e1\u01dc\3\2\2\2\u01e1\u01e0\3\2\2\2\u01e2s")
        buf.write("\3\2\2\2\u01e3\u01e4\7*\2\2\u01e4\u01e7\5t;\2\u01e5\u01e7")
        buf.write("\7*\2\2\u01e6\u01e3\3\2\2\2\u01e6\u01e5\3\2\2\2\u01e7")
        buf.write("u\3\2\2\2\u01e8\u01e9\7*\2\2\u01e9\u01ec\5v<\2\u01ea\u01ec")
        buf.write("\3\2\2\2\u01eb\u01e8\3\2\2\2\u01eb\u01ea\3\2\2\2\u01ec")
        buf.write("w\3\2\2\2+\177\u0083\u0087\u008d\u0095\u00a1\u00ad\u00b4")
        buf.write("\u00bb\u00c6\u00d6\u00dd\u00e3\u00e7\u00ea\u00f6\u00fa")
        buf.write("\u0104\u0108\u0111\u0118\u0121\u0136\u013c\u0145\u0159")
        buf.write("\u0165\u0179\u0180\u0187\u018e\u0198\u01a3\u01ae\u01b4")
        buf.write("\u01b9\u01c2\u01cc\u01e1\u01e6\u01eb")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'number'", "'bool'", "'string'", "'var'", 
                     "'dynamic'", "'return'", "'func'", "'for'", "'until'", 
                     "'by'", "'break'", "'continue'", "'if'", "'else'", 
                     "'elif'", "'begin'", "'end'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'='", "'!='", "'<-'", "'<'", "'<='", 
                     "'>'", "'>='", "'...'", "'=='", "'not'", "'and'", "'or'", 
                     "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "TYPE_NUMBER", "TYPE_BOOL", "TYPE_STRING", 
                      "VAR", "DYNAMIC", "RETURN", "FUNCTION", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MODULO", 
                      "EQUAL", "NOT_EQUAL", "ASSIGNMENT", "LESS_THAN", "LESS_THAN_OR_EQUAL", 
                      "GREATER_THAN", "GREATER_THAN_OR_EQUAL", "STRING_CONCATENATION", 
                      "STRING_COMPARISION", "NOT", "AND", "OR", "LEFT_PARENTHESIS", 
                      "RIGHT_PARENTHESIS", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
                      "COMMA", "NEWLINE", "UNCLOSE_STRING", "NUMBER", "BOOLEAN", 
                      "STRING", "COMMENT", "IDENTIFIER", "WS", "ILLEGAL_ESCAPE", 
                      "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_declaration_list = 1
    RULE_declaration = 2
    RULE_variable_declaration = 3
    RULE_primitive_type = 4
    RULE_impicit_type = 5
    RULE_array_declaration = 6
    RULE_array_size = 7
    RULE_array_size_list = 8
    RULE_array_value = 9
    RULE_multi_dimension_value = 10
    RULE_single_dimension_value = 11
    RULE_array_element_list = 12
    RULE_function_declaration = 13
    RULE_parameter_declaration = 14
    RULE_parameter_list = 15
    RULE_extra_parameter = 16
    RULE_parameter = 17
    RULE_function_body = 18
    RULE_block = 19
    RULE_statement_list = 20
    RULE_statement = 21
    RULE_simple_statement = 22
    RULE_conditional_statement = 23
    RULE_open_statement = 24
    RULE_close_statement = 25
    RULE_open_if = 26
    RULE_close_if = 27
    RULE_open_else = 28
    RULE_close_else = 29
    RULE_open_elif_list = 30
    RULE_close_elif_list = 31
    RULE_open_elif = 32
    RULE_close_elif = 33
    RULE_for_statement = 34
    RULE_assignment_statement = 35
    RULE_return_statement = 36
    RULE_break_statement = 37
    RULE_continue_statement = 38
    RULE_function_call_statement = 39
    RULE_function_call = 40
    RULE_argument_list = 41
    RULE_extra_argument_list = 42
    RULE_expression = 43
    RULE_expression1 = 44
    RULE_expression2 = 45
    RULE_expression3 = 46
    RULE_expression4 = 47
    RULE_expression5 = 48
    RULE_expression6 = 49
    RULE_expression7 = 50
    RULE_sub_expression = 51
    RULE_relational_operator = 52
    RULE_element_extract_expression = 53
    RULE_function_extract_expression = 54
    RULE_array_extract_expression = 55
    RULE_index_operators = 56
    RULE_newline_list = 57
    RULE_nullable_newline_list = 58

    ruleNames =  [ "program", "declaration_list", "declaration", "variable_declaration", 
                   "primitive_type", "impicit_type", "array_declaration", 
                   "array_size", "array_size_list", "array_value", "multi_dimension_value", 
                   "single_dimension_value", "array_element_list", "function_declaration", 
                   "parameter_declaration", "parameter_list", "extra_parameter", 
                   "parameter", "function_body", "block", "statement_list", 
                   "statement", "simple_statement", "conditional_statement", 
                   "open_statement", "close_statement", "open_if", "close_if", 
                   "open_else", "close_else", "open_elif_list", "close_elif_list", 
                   "open_elif", "close_elif", "for_statement", "assignment_statement", 
                   "return_statement", "break_statement", "continue_statement", 
                   "function_call_statement", "function_call", "argument_list", 
                   "extra_argument_list", "expression", "expression1", "expression2", 
                   "expression3", "expression4", "expression5", "expression6", 
                   "expression7", "sub_expression", "relational_operator", 
                   "element_extract_expression", "function_extract_expression", 
                   "array_extract_expression", "index_operators", "newline_list", 
                   "nullable_newline_list" ]

    EOF = Token.EOF
    TYPE_NUMBER=1
    TYPE_BOOL=2
    TYPE_STRING=3
    VAR=4
    DYNAMIC=5
    RETURN=6
    FUNCTION=7
    FOR=8
    UNTIL=9
    BY=10
    BREAK=11
    CONTINUE=12
    IF=13
    ELSE=14
    ELIF=15
    BEGIN=16
    END=17
    PLUS=18
    MINUS=19
    MULTIPLY=20
    DIVIDE=21
    MODULO=22
    EQUAL=23
    NOT_EQUAL=24
    ASSIGNMENT=25
    LESS_THAN=26
    LESS_THAN_OR_EQUAL=27
    GREATER_THAN=28
    GREATER_THAN_OR_EQUAL=29
    STRING_CONCATENATION=30
    STRING_COMPARISION=31
    NOT=32
    AND=33
    OR=34
    LEFT_PARENTHESIS=35
    RIGHT_PARENTHESIS=36
    LEFT_SQUARE_BRACKET=37
    RIGHT_SQUARE_BRACKET=38
    COMMA=39
    NEWLINE=40
    UNCLOSE_STRING=41
    NUMBER=42
    BOOLEAN=43
    STRING=44
    COMMENT=45
    IDENTIFIER=46
    WS=47
    ILLEGAL_ESCAPE=48
    ERROR_TOKEN=49

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_list(self):
            return self.getTypedRuleContext(ZCodeParser.Declaration_listContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.declaration_list()
            self.state = 119
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(ZCodeParser.DeclarationContext,0)


        def declaration_list(self):
            return self.getTypedRuleContext(ZCodeParser.Declaration_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_list" ):
                return visitor.visitDeclaration_list(self)
            else:
                return visitor.visitChildren(self)




    def declaration_list(self):

        localctx = ZCodeParser.Declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration_list)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.declaration()
                self.state = 122
                self.declaration_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_declarationContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Function_declarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = ZCodeParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TYPE_NUMBER, ZCodeParser.TYPE_BOOL, ZCodeParser.TYPE_STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.variable_declaration()
                pass
            elif token in [ZCodeParser.FUNCTION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.function_declaration()
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


    class Variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(ZCodeParser.Primitive_typeContext,0)


        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def ASSIGNMENT(self):
            return self.getToken(ZCodeParser.ASSIGNMENT, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def impicit_type(self):
            return self.getTypedRuleContext(ZCodeParser.Impicit_typeContext,0)


        def array_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Array_declarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variable_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = ZCodeParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable_declaration)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.TYPE_NUMBER, ZCodeParser.TYPE_BOOL, ZCodeParser.TYPE_STRING]:
                    self.state = 131
                    self.primitive_type()
                    pass
                elif token in [ZCodeParser.DYNAMIC]:
                    self.state = 132
                    self.match(ZCodeParser.DYNAMIC)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 135
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 136
                self.newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.TYPE_NUMBER, ZCodeParser.TYPE_BOOL, ZCodeParser.TYPE_STRING]:
                    self.state = 137
                    self.primitive_type()
                    pass
                elif token in [ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                    self.state = 138
                    self.impicit_type()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 141
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 142
                self.match(ZCodeParser.ASSIGNMENT)
                self.state = 143
                self.expression()
                self.state = 144
                self.newline_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 146
                self.array_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_NUMBER(self):
            return self.getToken(ZCodeParser.TYPE_NUMBER, 0)

        def TYPE_STRING(self):
            return self.getToken(ZCodeParser.TYPE_STRING, 0)

        def TYPE_BOOL(self):
            return self.getToken(ZCodeParser.TYPE_BOOL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = ZCodeParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TYPE_NUMBER) | (1 << ZCodeParser.TYPE_BOOL) | (1 << ZCodeParser.TYPE_STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Impicit_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_impicit_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImpicit_type" ):
                return visitor.visitImpicit_type(self)
            else:
                return visitor.visitChildren(self)




    def impicit_type(self):

        localctx = ZCodeParser.Impicit_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_impicit_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.VAR or _la==ZCodeParser.DYNAMIC):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(ZCodeParser.Primitive_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_size(self):
            return self.getTypedRuleContext(ZCodeParser.Array_sizeContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def ASSIGNMENT(self):
            return self.getToken(ZCodeParser.ASSIGNMENT, 0)

        def array_value(self):
            return self.getTypedRuleContext(ZCodeParser.Array_valueContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_declaration" ):
                return visitor.visitArray_declaration(self)
            else:
                return visitor.visitChildren(self)




    def array_declaration(self):

        localctx = ZCodeParser.Array_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.primitive_type()
            self.state = 154
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 155
            self.array_size()
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGNMENT]:
                self.state = 156
                self.match(ZCodeParser.ASSIGNMENT)
                self.state = 157
                self.array_value()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 161
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_sizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_SQUARE_BRACKET, 0)

        def array_size_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_size_listContext,0)


        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_SQUARE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_size

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_size" ):
                return visitor.visitArray_size(self)
            else:
                return visitor.visitChildren(self)




    def array_size(self):

        localctx = ZCodeParser.Array_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
            self.state = 164
            self.array_size_list()
            self.state = 165
            self.match(ZCodeParser.RIGHT_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_size_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def array_size_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_size_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_size_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_size_list" ):
                return visitor.visitArray_size_list(self)
            else:
                return visitor.visitChildren(self)




    def array_size_list(self):

        localctx = ZCodeParser.Array_size_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_size_list)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(ZCodeParser.NUMBER)
                self.state = 168
                self.match(ZCodeParser.COMMA)
                self.state = 169
                self.array_size_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.match(ZCodeParser.NUMBER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_dimension_value(self):
            return self.getTypedRuleContext(ZCodeParser.Single_dimension_valueContext,0)


        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_SQUARE_BRACKET, 0)

        def multi_dimension_value(self):
            return self.getTypedRuleContext(ZCodeParser.Multi_dimension_valueContext,0)


        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_SQUARE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_value" ):
                return visitor.visitArray_value(self)
            else:
                return visitor.visitChildren(self)




    def array_value(self):

        localctx = ZCodeParser.Array_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_value)
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.single_dimension_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
                self.state = 175
                self.multi_dimension_value()
                self.state = 176
                self.match(ZCodeParser.RIGHT_SQUARE_BRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multi_dimension_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_dimension_value(self):
            return self.getTypedRuleContext(ZCodeParser.Single_dimension_valueContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def multi_dimension_value(self):
            return self.getTypedRuleContext(ZCodeParser.Multi_dimension_valueContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_multi_dimension_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulti_dimension_value" ):
                return visitor.visitMulti_dimension_value(self)
            else:
                return visitor.visitChildren(self)




    def multi_dimension_value(self):

        localctx = ZCodeParser.Multi_dimension_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_multi_dimension_value)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.single_dimension_value()
                self.state = 181
                self.match(ZCodeParser.COMMA)
                self.state = 182
                self.multi_dimension_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.single_dimension_value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_dimension_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_SQUARE_BRACKET, 0)

        def array_element_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_element_listContext,0)


        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_SQUARE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_single_dimension_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle_dimension_value" ):
                return visitor.visitSingle_dimension_value(self)
            else:
                return visitor.visitChildren(self)




    def single_dimension_value(self):

        localctx = ZCodeParser.Single_dimension_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_single_dimension_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
            self.state = 188
            self.array_element_list()
            self.state = 189
            self.match(ZCodeParser.RIGHT_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_element_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def array_element_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_element_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_element_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element_list" ):
                return visitor.visitArray_element_list(self)
            else:
                return visitor.visitChildren(self)




    def array_element_list(self):

        localctx = ZCodeParser.Array_element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_array_element_list)
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.expression()
                self.state = 192
                self.match(ZCodeParser.COMMA)
                self.state = 193
                self.array_element_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(ZCodeParser.FUNCTION, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def parameter_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_declarationContext,0)


        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def function_body(self):
            return self.getTypedRuleContext(ZCodeParser.Function_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = ZCodeParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_function_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(ZCodeParser.FUNCTION)
            self.state = 199
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 200
            self.parameter_declaration()
            self.state = 201
            self.nullable_newline_list()
            self.state = 202
            self.function_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.LEFT_PARENTHESIS, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_listContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.RIGHT_PARENTHESIS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_declaration" ):
                return visitor.visitParameter_declaration(self)
            else:
                return visitor.visitChildren(self)




    def parameter_declaration(self):

        localctx = ZCodeParser.Parameter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_parameter_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(ZCodeParser.LEFT_PARENTHESIS)
            self.state = 205
            self.parameter_list()
            self.state = 206
            self.match(ZCodeParser.RIGHT_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterContext,0)


        def extra_parameter(self):
            return self.getTypedRuleContext(ZCodeParser.Extra_parameterContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = ZCodeParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_parameter_list)
        try:
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TYPE_NUMBER, ZCodeParser.TYPE_BOOL, ZCodeParser.TYPE_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.parameter()
                self.state = 209
                self.extra_parameter()
                pass
            elif token in [ZCodeParser.RIGHT_PARENTHESIS]:
                self.enterOuterAlt(localctx, 2)

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


    class Extra_parameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def parameter(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterContext,0)


        def extra_parameter(self):
            return self.getTypedRuleContext(ZCodeParser.Extra_parameterContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_extra_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtra_parameter" ):
                return visitor.visitExtra_parameter(self)
            else:
                return visitor.visitChildren(self)




    def extra_parameter(self):

        localctx = ZCodeParser.Extra_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_extra_parameter)
        try:
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(ZCodeParser.COMMA)
                self.state = 215
                self.parameter()
                self.state = 216
                self.extra_parameter()
                pass
            elif token in [ZCodeParser.RIGHT_PARENTHESIS]:
                self.enterOuterAlt(localctx, 2)

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


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(ZCodeParser.Primitive_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_size(self):
            return self.getTypedRuleContext(ZCodeParser.Array_sizeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = ZCodeParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.primitive_type()
            self.state = 222
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LEFT_SQUARE_BRACKET]:
                self.state = 223
                self.array_size()
                pass
            elif token in [ZCodeParser.RIGHT_PARENTHESIS, ZCodeParser.COMMA]:
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


    class Function_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(ZCodeParser.BlockContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_body" ):
                return visitor.visitFunction_body(self)
            else:
                return visitor.visitChildren(self)




    def function_body(self):

        localctx = ZCodeParser.Function_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_function_body)
        try:
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN, ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.BEGIN]:
                    self.state = 227
                    self.block()
                    pass
                elif token in [ZCodeParser.RETURN]:
                    self.state = 228
                    self.return_statement()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.newline_list()
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


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def newline_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Newline_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Newline_listContext,i)


        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = ZCodeParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(ZCodeParser.BEGIN)
            self.state = 235
            self.newline_list()
            self.state = 236
            self.statement_list()
            self.state = 237
            self.match(ZCodeParser.END)
            self.state = 238
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)




    def statement_list(self):

        localctx = ZCodeParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_statement_list)
        try:
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TYPE_NUMBER, ZCodeParser.TYPE_BOOL, ZCodeParser.TYPE_STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.RETURN, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.statement()
                self.state = 241
                self.statement_list()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Simple_statementContext,0)


        def conditional_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Conditional_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_statement)
        try:
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.simple_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.conditional_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_declarationContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Assignment_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def function_call_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Function_call_statementContext,0)


        def block(self):
            return self.getTypedRuleContext(ZCodeParser.BlockContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(ZCodeParser.For_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_simple_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_statement" ):
                return visitor.visitSimple_statement(self)
            else:
                return visitor.visitChildren(self)




    def simple_statement(self):

        localctx = ZCodeParser.Simple_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_simple_statement)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.break_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 253
                self.continue_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 254
                self.return_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 255
                self.function_call_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 256
                self.block()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 257
                self.for_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def open_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Open_statementContext,0)


        def close_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Close_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_conditional_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional_statement" ):
                return visitor.visitConditional_statement(self)
            else:
                return visitor.visitChildren(self)




    def conditional_statement(self):

        localctx = ZCodeParser.Conditional_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_conditional_statement)
        try:
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.open_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.close_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Open_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def open_if(self):
            return self.getTypedRuleContext(ZCodeParser.Open_ifContext,0)


        def open_elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Open_elif_listContext,0)


        def close_if(self):
            return self.getTypedRuleContext(ZCodeParser.Close_ifContext,0)


        def close_elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Close_elif_listContext,0)


        def open_else(self):
            return self.getTypedRuleContext(ZCodeParser.Open_elseContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_open_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpen_statement" ):
                return visitor.visitOpen_statement(self)
            else:
                return visitor.visitChildren(self)




    def open_statement(self):

        localctx = ZCodeParser.Open_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_open_statement)
        try:
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.open_if()
                self.state = 265
                self.open_elif_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.close_if()
                self.state = 268
                self.close_elif_list()
                self.state = 269
                self.open_else()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Close_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Simple_statementContext,0)


        def close_if(self):
            return self.getTypedRuleContext(ZCodeParser.Close_ifContext,0)


        def close_elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Close_elif_listContext,0)


        def close_else(self):
            return self.getTypedRuleContext(ZCodeParser.Close_elseContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_close_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClose_statement" ):
                return visitor.visitClose_statement(self)
            else:
                return visitor.visitChildren(self)




    def close_statement(self):

        localctx = ZCodeParser.Close_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_close_statement)
        try:
            self.state = 278
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TYPE_NUMBER, ZCodeParser.TYPE_BOOL, ZCodeParser.TYPE_STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.RETURN, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.simple_statement()
                pass
            elif token in [ZCodeParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.close_if()
                self.state = 275
                self.close_elif_list()
                self.state = 276
                self.close_else()
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


    class Open_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.LEFT_PARENTHESIS, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.RIGHT_PARENTHESIS, 0)

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def simple_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Simple_statementContext,0)


        def open_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Open_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_open_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpen_if" ):
                return visitor.visitOpen_if(self)
            else:
                return visitor.visitChildren(self)




    def open_if(self):

        localctx = ZCodeParser.Open_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_open_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(ZCodeParser.IF)
            self.state = 281
            self.match(ZCodeParser.LEFT_PARENTHESIS)
            self.state = 282
            self.expression()
            self.state = 283
            self.match(ZCodeParser.RIGHT_PARENTHESIS)
            self.state = 284
            self.nullable_newline_list()
            self.state = 287
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TYPE_NUMBER, ZCodeParser.TYPE_BOOL, ZCodeParser.TYPE_STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.RETURN, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.state = 285
                self.simple_statement()
                pass
            elif token in [ZCodeParser.IF]:
                self.state = 286
                self.open_statement()
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


    class Close_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.LEFT_PARENTHESIS, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.RIGHT_PARENTHESIS, 0)

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def close_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Close_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_close_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClose_if" ):
                return visitor.visitClose_if(self)
            else:
                return visitor.visitChildren(self)




    def close_if(self):

        localctx = ZCodeParser.Close_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_close_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(ZCodeParser.IF)
            self.state = 290
            self.match(ZCodeParser.LEFT_PARENTHESIS)
            self.state = 291
            self.expression()
            self.state = 292
            self.match(ZCodeParser.RIGHT_PARENTHESIS)
            self.state = 293
            self.nullable_newline_list()
            self.state = 294
            self.close_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Open_elseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def open_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Open_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_open_else

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpen_else" ):
                return visitor.visitOpen_else(self)
            else:
                return visitor.visitChildren(self)




    def open_else(self):

        localctx = ZCodeParser.Open_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_open_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(ZCodeParser.ELSE)
            self.state = 297
            self.nullable_newline_list()
            self.state = 298
            self.open_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Close_elseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def close_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Close_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_close_else

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClose_else" ):
                return visitor.visitClose_else(self)
            else:
                return visitor.visitChildren(self)




    def close_else(self):

        localctx = ZCodeParser.Close_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_close_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(ZCodeParser.ELSE)
            self.state = 301
            self.nullable_newline_list()
            self.state = 302
            self.close_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Open_elif_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def open_elif(self):
            return self.getTypedRuleContext(ZCodeParser.Open_elifContext,0)


        def open_elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Open_elif_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_open_elif_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpen_elif_list" ):
                return visitor.visitOpen_elif_list(self)
            else:
                return visitor.visitChildren(self)




    def open_elif_list(self):

        localctx = ZCodeParser.Open_elif_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_open_elif_list)
        try:
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.open_elif()
                self.state = 305
                self.open_elif_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Close_elif_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def close_elif(self):
            return self.getTypedRuleContext(ZCodeParser.Close_elifContext,0)


        def close_elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Close_elif_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_close_elif_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClose_elif_list" ):
                return visitor.visitClose_elif_list(self)
            else:
                return visitor.visitChildren(self)




    def close_elif_list(self):

        localctx = ZCodeParser.Close_elif_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_close_elif_list)
        try:
            self.state = 314
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ELIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.close_elif()
                self.state = 311
                self.close_elif_list()
                pass
            elif token in [ZCodeParser.ELSE]:
                self.enterOuterAlt(localctx, 2)

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


    class Open_elifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.LEFT_PARENTHESIS, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.RIGHT_PARENTHESIS, 0)

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def simple_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Simple_statementContext,0)


        def open_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Open_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_open_elif

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpen_elif" ):
                return visitor.visitOpen_elif(self)
            else:
                return visitor.visitChildren(self)




    def open_elif(self):

        localctx = ZCodeParser.Open_elifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_open_elif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(ZCodeParser.ELIF)
            self.state = 317
            self.match(ZCodeParser.LEFT_PARENTHESIS)
            self.state = 318
            self.expression()
            self.state = 319
            self.match(ZCodeParser.RIGHT_PARENTHESIS)
            self.state = 320
            self.nullable_newline_list()
            self.state = 323
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TYPE_NUMBER, ZCodeParser.TYPE_BOOL, ZCodeParser.TYPE_STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.RETURN, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.state = 321
                self.simple_statement()
                pass
            elif token in [ZCodeParser.IF]:
                self.state = 322
                self.open_statement()
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


    class Close_elifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.LEFT_PARENTHESIS, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.RIGHT_PARENTHESIS, 0)

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def close_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Close_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_close_elif

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClose_elif" ):
                return visitor.visitClose_elif(self)
            else:
                return visitor.visitChildren(self)




    def close_elif(self):

        localctx = ZCodeParser.Close_elifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_close_elif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(ZCodeParser.ELIF)
            self.state = 326
            self.match(ZCodeParser.LEFT_PARENTHESIS)
            self.state = 327
            self.expression()
            self.state = 328
            self.match(ZCodeParser.RIGHT_PARENTHESIS)
            self.state = 329
            self.nullable_newline_list()
            self.state = 330
            self.close_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = ZCodeParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(ZCodeParser.FOR)
            self.state = 333
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 334
            self.match(ZCodeParser.UNTIL)
            self.state = 335
            self.expression()
            self.state = 336
            self.match(ZCodeParser.BY)
            self.state = 337
            self.expression()
            self.state = 338
            self.nullable_newline_list()
            self.state = 339
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGNMENT(self):
            return self.getToken(ZCodeParser.ASSIGNMENT, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_extract_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Array_extract_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = ZCodeParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 341
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 342
                self.array_extract_expression()
                pass


            self.state = 345
            self.match(ZCodeParser.ASSIGNMENT)
            self.state = 346
            self.expression()
            self.state = 347
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_return_statement)
        try:
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.match(ZCodeParser.RETURN)
                self.state = 350
                self.expression()
                self.state = 351
                self.newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.match(ZCodeParser.RETURN)
                self.state = 354
                self.newline_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(ZCodeParser.BREAK)
            self.state = 358
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(ZCodeParser.CONTINUE)
            self.state = 361
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(ZCodeParser.Function_callContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_statement" ):
                return visitor.visitFunction_call_statement(self)
            else:
                return visitor.visitChildren(self)




    def function_call_statement(self):

        localctx = ZCodeParser.Function_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_function_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.function_call()
            self.state = 364
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.LEFT_PARENTHESIS, 0)

        def argument_list(self):
            return self.getTypedRuleContext(ZCodeParser.Argument_listContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.RIGHT_PARENTHESIS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = ZCodeParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 367
            self.match(ZCodeParser.LEFT_PARENTHESIS)
            self.state = 368
            self.argument_list()
            self.state = 369
            self.match(ZCodeParser.RIGHT_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def extra_argument_list(self):
            return self.getTypedRuleContext(ZCodeParser.Extra_argument_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argument_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_list" ):
                return visitor.visitArgument_list(self)
            else:
                return visitor.visitChildren(self)




    def argument_list(self):

        localctx = ZCodeParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_argument_list)
        try:
            self.state = 375
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS, ZCodeParser.NOT, ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.NUMBER, ZCodeParser.BOOLEAN, ZCodeParser.STRING, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.expression()
                self.state = 372
                self.extra_argument_list()
                pass
            elif token in [ZCodeParser.RIGHT_PARENTHESIS]:
                self.enterOuterAlt(localctx, 2)

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


    class Extra_argument_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def extra_argument_list(self):
            return self.getTypedRuleContext(ZCodeParser.Extra_argument_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_extra_argument_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtra_argument_list" ):
                return visitor.visitExtra_argument_list(self)
            else:
                return visitor.visitChildren(self)




    def extra_argument_list(self):

        localctx = ZCodeParser.Extra_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_extra_argument_list)
        try:
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.match(ZCodeParser.COMMA)
                self.state = 378
                self.expression()
                self.state = 379
                self.extra_argument_list()
                pass
            elif token in [ZCodeParser.RIGHT_PARENTHESIS]:
                self.enterOuterAlt(localctx, 2)

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


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression1Context,i)


        def STRING_CONCATENATION(self):
            return self.getToken(ZCodeParser.STRING_CONCATENATION, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expression)
        try:
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.expression1()
                self.state = 385
                self.match(ZCodeParser.STRING_CONCATENATION)
                self.state = 386
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.expression1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression2Context,i)


        def relational_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Relational_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)




    def expression1(self):

        localctx = ZCodeParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expression1)
        try:
            self.state = 396
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.expression2(0)
                self.state = 392
                self.relational_operator()
                self.state = 393
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.expression2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(ZCodeParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(ZCodeParser.Expression2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 406
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 401
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 402
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 403
                    self.expression3(0) 
                self.state = 408
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(ZCodeParser.Expression3Context,0)


        def PLUS(self):
            return self.getToken(ZCodeParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 417
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 412
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 413
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 414
                    self.expression4(0) 
                self.state = 419
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression4Context,0)


        def MULTIPLY(self):
            return self.getToken(ZCodeParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(ZCodeParser.DIVIDE, 0)

        def MODULO(self):
            return self.getToken(ZCodeParser.MODULO, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 428
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 423
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 424
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MULTIPLY) | (1 << ZCodeParser.DIVIDE) | (1 << ZCodeParser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 425
                    self.expression5() 
                self.state = 430
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expression5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression5Context,0)


        def expression6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = ZCodeParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_expression5)
        try:
            self.state = 434
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 431
                self.match(ZCodeParser.NOT)
                self.state = 432
                self.expression5()
                pass
            elif token in [ZCodeParser.MINUS, ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.NUMBER, ZCodeParser.BOOLEAN, ZCodeParser.STRING, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 433
                self.expression6()
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


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def expression6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression6Context,0)


        def expression7(self):
            return self.getTypedRuleContext(ZCodeParser.Expression7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)




    def expression6(self):

        localctx = ZCodeParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_expression6)
        try:
            self.state = 439
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.match(ZCodeParser.MINUS)
                self.state = 437
                self.expression6()
                pass
            elif token in [ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.NUMBER, ZCodeParser.BOOLEAN, ZCodeParser.STRING, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
                self.expression7()
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


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOLEAN(self):
            return self.getToken(ZCodeParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def element_extract_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Element_extract_expressionContext,0)


        def function_call(self):
            return self.getTypedRuleContext(ZCodeParser.Function_callContext,0)


        def sub_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Sub_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = ZCodeParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_expression7)
        try:
            self.state = 448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 442
                self.match(ZCodeParser.BOOLEAN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 443
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 444
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 445
                self.element_extract_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 446
                self.function_call()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 447
                self.sub_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sub_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.LEFT_PARENTHESIS, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.RIGHT_PARENTHESIS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_sub_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub_expression" ):
                return visitor.visitSub_expression(self)
            else:
                return visitor.visitChildren(self)




    def sub_expression(self):

        localctx = ZCodeParser.Sub_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_sub_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(ZCodeParser.LEFT_PARENTHESIS)
            self.state = 451
            self.expression()
            self.state = 452
            self.match(ZCodeParser.RIGHT_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def STRING_COMPARISION(self):
            return self.getToken(ZCodeParser.STRING_COMPARISION, 0)

        def NOT_EQUAL(self):
            return self.getToken(ZCodeParser.NOT_EQUAL, 0)

        def LESS_THAN(self):
            return self.getToken(ZCodeParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(ZCodeParser.GREATER_THAN, 0)

        def LESS_THAN_OR_EQUAL(self):
            return self.getToken(ZCodeParser.LESS_THAN_OR_EQUAL, 0)

        def GREATER_THAN_OR_EQUAL(self):
            return self.getToken(ZCodeParser.GREATER_THAN_OR_EQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_relational_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_operator" ):
                return visitor.visitRelational_operator(self)
            else:
                return visitor.visitChildren(self)




    def relational_operator(self):

        localctx = ZCodeParser.Relational_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_relational_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.NOT_EQUAL) | (1 << ZCodeParser.LESS_THAN) | (1 << ZCodeParser.LESS_THAN_OR_EQUAL) | (1 << ZCodeParser.GREATER_THAN) | (1 << ZCodeParser.GREATER_THAN_OR_EQUAL) | (1 << ZCodeParser.STRING_COMPARISION))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_extract_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_SQUARE_BRACKET, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_SQUARE_BRACKET, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def function_call(self):
            return self.getTypedRuleContext(ZCodeParser.Function_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_element_extract_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_extract_expression" ):
                return visitor.visitElement_extract_expression(self)
            else:
                return visitor.visitChildren(self)




    def element_extract_expression(self):

        localctx = ZCodeParser.Element_extract_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_element_extract_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 456
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 457
                self.function_call()
                pass


            self.state = 460
            self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
            self.state = 461
            self.index_operators()
            self.state = 462
            self.match(ZCodeParser.RIGHT_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_extract_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(ZCodeParser.Function_callContext,0)


        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_SQUARE_BRACKET, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_SQUARE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_function_extract_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_extract_expression" ):
                return visitor.visitFunction_extract_expression(self)
            else:
                return visitor.visitChildren(self)




    def function_extract_expression(self):

        localctx = ZCodeParser.Function_extract_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_function_extract_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.function_call()
            self.state = 465
            self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
            self.state = 466
            self.index_operators()
            self.state = 467
            self.match(ZCodeParser.RIGHT_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_extract_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_SQUARE_BRACKET, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_SQUARE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_extract_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_extract_expression" ):
                return visitor.visitArray_extract_expression(self)
            else:
                return visitor.visitChildren(self)




    def array_extract_expression(self):

        localctx = ZCodeParser.Array_extract_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_array_extract_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 470
            self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
            self.state = 471
            self.index_operators()
            self.state = 472
            self.match(ZCodeParser.RIGHT_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = ZCodeParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_index_operators)
        try:
            self.state = 479
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 474
                self.expression()
                self.state = 475
                self.match(ZCodeParser.COMMA)
                self.state = 476
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 478
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Newline_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newline_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline_list" ):
                return visitor.visitNewline_list(self)
            else:
                return visitor.visitChildren(self)




    def newline_list(self):

        localctx = ZCodeParser.Newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_newline_list)
        try:
            self.state = 484
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 481
                self.match(ZCodeParser.NEWLINE)
                self.state = 482
                self.newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 483
                self.match(ZCodeParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nullable_newline_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nullable_newline_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullable_newline_list" ):
                return visitor.visitNullable_newline_list(self)
            else:
                return visitor.visitChildren(self)




    def nullable_newline_list(self):

        localctx = ZCodeParser.Nullable_newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_nullable_newline_list)
        try:
            self.state = 489
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 486
                self.match(ZCodeParser.NEWLINE)
                self.state = 487
                self.nullable_newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[45] = self.expression2_sempred
        self._predicates[46] = self.expression3_sempred
        self._predicates[47] = self.expression4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




