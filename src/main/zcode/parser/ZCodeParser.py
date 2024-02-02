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
        buf.write("\u01ea\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\3+\3")
        buf.write("+\5+\u0176\n+\3,\3,\3,\3,\3,\5,\u017d\n,\3-\3-\3-\3-\3")
        buf.write("-\5-\u0184\n-\3.\3.\3.\3.\3.\5.\u018b\n.\3/\3/\3/\3/\3")
        buf.write("/\3/\7/\u0193\n/\f/\16/\u0196\13/\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\7\60\u019e\n\60\f\60\16\60\u01a1\13\60\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\7\61\u01a9\n\61\f\61\16\61\u01ac")
        buf.write("\13\61\3\62\3\62\3\62\5\62\u01b1\n\62\3\63\3\63\3\63\5")
        buf.write("\63\u01b6\n\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64")
        buf.write("\u01bf\n\64\3\65\3\65\3\65\3\65\3\66\3\66\3\67\3\67\5")
        buf.write("\67\u01c9\n\67\3\67\3\67\3\67\3\67\38\38\38\38\38\39\3")
        buf.write("9\39\39\39\3:\3:\3:\3:\3:\5:\u01de\n:\3;\3;\3;\5;\u01e3")
        buf.write("\n;\3<\3<\3<\5<\u01e8\n<\3<\2\5\\^`=\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\\^`bdfhjlnprtv\2\b\3\2\3\5\3\2\6\7\3\2#$\3\2\24")
        buf.write("\25\3\2\26\30\5\2\31\32\34\37!!\2\u01e2\2x\3\2\2\2\4\177")
        buf.write("\3\2\2\2\6\u0083\3\2\2\2\b\u0095\3\2\2\2\n\u0097\3\2\2")
        buf.write("\2\f\u0099\3\2\2\2\16\u009b\3\2\2\2\20\u00a5\3\2\2\2\22")
        buf.write("\u00ad\3\2\2\2\24\u00b4\3\2\2\2\26\u00bb\3\2\2\2\30\u00bd")
        buf.write("\3\2\2\2\32\u00c6\3\2\2\2\34\u00c8\3\2\2\2\36\u00ce\3")
        buf.write("\2\2\2 \u00d6\3\2\2\2\"\u00dd\3\2\2\2$\u00df\3\2\2\2&")
        buf.write("\u00ea\3\2\2\2(\u00ec\3\2\2\2*\u00f6\3\2\2\2,\u00fa\3")
        buf.write("\2\2\2.\u0104\3\2\2\2\60\u0108\3\2\2\2\62\u0111\3\2\2")
        buf.write("\2\64\u0118\3\2\2\2\66\u011a\3\2\2\28\u0123\3\2\2\2:\u012a")
        buf.write("\3\2\2\2<\u012e\3\2\2\2>\u0136\3\2\2\2@\u013c\3\2\2\2")
        buf.write("B\u013e\3\2\2\2D\u0147\3\2\2\2F\u014e\3\2\2\2H\u0159\3")
        buf.write("\2\2\2J\u015f\3\2\2\2L\u0163\3\2\2\2N\u0166\3\2\2\2P\u0169")
        buf.write("\3\2\2\2R\u016c\3\2\2\2T\u0175\3\2\2\2V\u017c\3\2\2\2")
        buf.write("X\u0183\3\2\2\2Z\u018a\3\2\2\2\\\u018c\3\2\2\2^\u0197")
        buf.write("\3\2\2\2`\u01a2\3\2\2\2b\u01b0\3\2\2\2d\u01b5\3\2\2\2")
        buf.write("f\u01be\3\2\2\2h\u01c0\3\2\2\2j\u01c4\3\2\2\2l\u01c8\3")
        buf.write("\2\2\2n\u01ce\3\2\2\2p\u01d3\3\2\2\2r\u01dd\3\2\2\2t\u01e2")
        buf.write("\3\2\2\2v\u01e7\3\2\2\2xy\5\4\3\2yz\7\2\2\3z\3\3\2\2\2")
        buf.write("{|\5\6\4\2|}\5\4\3\2}\u0080\3\2\2\2~\u0080\5\6\4\2\177")
        buf.write("{\3\2\2\2\177~\3\2\2\2\u0080\5\3\2\2\2\u0081\u0084\5\b")
        buf.write("\5\2\u0082\u0084\5\34\17\2\u0083\u0081\3\2\2\2\u0083\u0082")
        buf.write("\3\2\2\2\u0084\7\3\2\2\2\u0085\u0088\5\n\6\2\u0086\u0088")
        buf.write("\7\7\2\2\u0087\u0085\3\2\2\2\u0087\u0086\3\2\2\2\u0088")
        buf.write("\u0089\3\2\2\2\u0089\u008a\7/\2\2\u008a\u0096\5t;\2\u008b")
        buf.write("\u008e\5\n\6\2\u008c\u008e\5\f\7\2\u008d\u008b\3\2\2\2")
        buf.write("\u008d\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0090\7")
        buf.write("/\2\2\u0090\u0091\7\33\2\2\u0091\u0092\5X-\2\u0092\u0093")
        buf.write("\5t;\2\u0093\u0096\3\2\2\2\u0094\u0096\5\16\b\2\u0095")
        buf.write("\u0087\3\2\2\2\u0095\u008d\3\2\2\2\u0095\u0094\3\2\2\2")
        buf.write("\u0096\t\3\2\2\2\u0097\u0098\t\2\2\2\u0098\13\3\2\2\2")
        buf.write("\u0099\u009a\t\3\2\2\u009a\r\3\2\2\2\u009b\u009c\5\n\6")
        buf.write("\2\u009c\u009d\7/\2\2\u009d\u00a1\5\20\t\2\u009e\u009f")
        buf.write("\7\33\2\2\u009f\u00a2\5\24\13\2\u00a0\u00a2\3\2\2\2\u00a1")
        buf.write("\u009e\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2")
        buf.write("\u00a3\u00a4\5t;\2\u00a4\17\3\2\2\2\u00a5\u00a6\7\'\2")
        buf.write("\2\u00a6\u00a7\5\22\n\2\u00a7\u00a8\7(\2\2\u00a8\21\3")
        buf.write("\2\2\2\u00a9\u00aa\7+\2\2\u00aa\u00ab\7)\2\2\u00ab\u00ae")
        buf.write("\5\22\n\2\u00ac\u00ae\7+\2\2\u00ad\u00a9\3\2\2\2\u00ad")
        buf.write("\u00ac\3\2\2\2\u00ae\23\3\2\2\2\u00af\u00b5\5\30\r\2\u00b0")
        buf.write("\u00b1\7\'\2\2\u00b1\u00b2\5\26\f\2\u00b2\u00b3\7(\2\2")
        buf.write("\u00b3\u00b5\3\2\2\2\u00b4\u00af\3\2\2\2\u00b4\u00b0\3")
        buf.write("\2\2\2\u00b5\25\3\2\2\2\u00b6\u00b7\5\30\r\2\u00b7\u00b8")
        buf.write("\7)\2\2\u00b8\u00b9\5\26\f\2\u00b9\u00bc\3\2\2\2\u00ba")
        buf.write("\u00bc\5\30\r\2\u00bb\u00b6\3\2\2\2\u00bb\u00ba\3\2\2")
        buf.write("\2\u00bc\27\3\2\2\2\u00bd\u00be\7\'\2\2\u00be\u00bf\5")
        buf.write("\32\16\2\u00bf\u00c0\7(\2\2\u00c0\31\3\2\2\2\u00c1\u00c2")
        buf.write("\5X-\2\u00c2\u00c3\7)\2\2\u00c3\u00c4\5\32\16\2\u00c4")
        buf.write("\u00c7\3\2\2\2\u00c5\u00c7\5X-\2\u00c6\u00c1\3\2\2\2\u00c6")
        buf.write("\u00c5\3\2\2\2\u00c7\33\3\2\2\2\u00c8\u00c9\7\t\2\2\u00c9")
        buf.write("\u00ca\7/\2\2\u00ca\u00cb\5\36\20\2\u00cb\u00cc\5v<\2")
        buf.write("\u00cc\u00cd\5&\24\2\u00cd\35\3\2\2\2\u00ce\u00cf\7%\2")
        buf.write("\2\u00cf\u00d0\5 \21\2\u00d0\u00d1\7&\2\2\u00d1\37\3\2")
        buf.write("\2\2\u00d2\u00d3\5$\23\2\u00d3\u00d4\5\"\22\2\u00d4\u00d7")
        buf.write("\3\2\2\2\u00d5\u00d7\3\2\2\2\u00d6\u00d2\3\2\2\2\u00d6")
        buf.write("\u00d5\3\2\2\2\u00d7!\3\2\2\2\u00d8\u00d9\7)\2\2\u00d9")
        buf.write("\u00da\5$\23\2\u00da\u00db\5\"\22\2\u00db\u00de\3\2\2")
        buf.write("\2\u00dc\u00de\3\2\2\2\u00dd\u00d8\3\2\2\2\u00dd\u00dc")
        buf.write("\3\2\2\2\u00de#\3\2\2\2\u00df\u00e0\5\n\6\2\u00e0\u00e3")
        buf.write("\7/\2\2\u00e1\u00e4\5\20\t\2\u00e2\u00e4\3\2\2\2\u00e3")
        buf.write("\u00e1\3\2\2\2\u00e3\u00e2\3\2\2\2\u00e4%\3\2\2\2\u00e5")
        buf.write("\u00e8\5(\25\2\u00e6\u00e8\5J&\2\u00e7\u00e5\3\2\2\2\u00e7")
        buf.write("\u00e6\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9\u00eb\5t;\2\u00ea")
        buf.write("\u00e7\3\2\2\2\u00ea\u00e9\3\2\2\2\u00eb\'\3\2\2\2\u00ec")
        buf.write("\u00ed\7\22\2\2\u00ed\u00ee\5t;\2\u00ee\u00ef\5*\26\2")
        buf.write("\u00ef\u00f0\7\23\2\2\u00f0\u00f1\5t;\2\u00f1)\3\2\2\2")
        buf.write("\u00f2\u00f3\5,\27\2\u00f3\u00f4\5*\26\2\u00f4\u00f7\3")
        buf.write("\2\2\2\u00f5\u00f7\3\2\2\2\u00f6\u00f2\3\2\2\2\u00f6\u00f5")
        buf.write("\3\2\2\2\u00f7+\3\2\2\2\u00f8\u00fb\5.\30\2\u00f9\u00fb")
        buf.write("\5\60\31\2\u00fa\u00f8\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb")
        buf.write("-\3\2\2\2\u00fc\u0105\5\b\5\2\u00fd\u0105\5H%\2\u00fe")
        buf.write("\u0105\5L\'\2\u00ff\u0105\5N(\2\u0100\u0105\5J&\2\u0101")
        buf.write("\u0105\5P)\2\u0102\u0105\5(\25\2\u0103\u0105\5F$\2\u0104")
        buf.write("\u00fc\3\2\2\2\u0104\u00fd\3\2\2\2\u0104\u00fe\3\2\2\2")
        buf.write("\u0104\u00ff\3\2\2\2\u0104\u0100\3\2\2\2\u0104\u0101\3")
        buf.write("\2\2\2\u0104\u0102\3\2\2\2\u0104\u0103\3\2\2\2\u0105/")
        buf.write("\3\2\2\2\u0106\u0109\5\62\32\2\u0107\u0109\5\64\33\2\u0108")
        buf.write("\u0106\3\2\2\2\u0108\u0107\3\2\2\2\u0109\61\3\2\2\2\u010a")
        buf.write("\u010b\5\66\34\2\u010b\u010c\5> \2\u010c\u0112\3\2\2\2")
        buf.write("\u010d\u010e\58\35\2\u010e\u010f\5@!\2\u010f\u0110\5:")
        buf.write("\36\2\u0110\u0112\3\2\2\2\u0111\u010a\3\2\2\2\u0111\u010d")
        buf.write("\3\2\2\2\u0112\63\3\2\2\2\u0113\u0119\5.\30\2\u0114\u0115")
        buf.write("\58\35\2\u0115\u0116\5@!\2\u0116\u0117\5<\37\2\u0117\u0119")
        buf.write("\3\2\2\2\u0118\u0113\3\2\2\2\u0118\u0114\3\2\2\2\u0119")
        buf.write("\65\3\2\2\2\u011a\u011b\7\17\2\2\u011b\u011c\7%\2\2\u011c")
        buf.write("\u011d\5X-\2\u011d\u011e\7&\2\2\u011e\u0121\5v<\2\u011f")
        buf.write("\u0122\5.\30\2\u0120\u0122\5\62\32\2\u0121\u011f\3\2\2")
        buf.write("\2\u0121\u0120\3\2\2\2\u0122\67\3\2\2\2\u0123\u0124\7")
        buf.write("\17\2\2\u0124\u0125\7%\2\2\u0125\u0126\5X-\2\u0126\u0127")
        buf.write("\7&\2\2\u0127\u0128\5v<\2\u0128\u0129\5\64\33\2\u0129")
        buf.write("9\3\2\2\2\u012a\u012b\7\20\2\2\u012b\u012c\5v<\2\u012c")
        buf.write("\u012d\5\62\32\2\u012d;\3\2\2\2\u012e\u012f\7\20\2\2\u012f")
        buf.write("\u0130\5v<\2\u0130\u0131\5\64\33\2\u0131=\3\2\2\2\u0132")
        buf.write("\u0133\5B\"\2\u0133\u0134\5> \2\u0134\u0137\3\2\2\2\u0135")
        buf.write("\u0137\3\2\2\2\u0136\u0132\3\2\2\2\u0136\u0135\3\2\2\2")
        buf.write("\u0137?\3\2\2\2\u0138\u0139\5D#\2\u0139\u013a\5@!\2\u013a")
        buf.write("\u013d\3\2\2\2\u013b\u013d\3\2\2\2\u013c\u0138\3\2\2\2")
        buf.write("\u013c\u013b\3\2\2\2\u013dA\3\2\2\2\u013e\u013f\7\21\2")
        buf.write("\2\u013f\u0140\7%\2\2\u0140\u0141\5X-\2\u0141\u0142\7")
        buf.write("&\2\2\u0142\u0145\5v<\2\u0143\u0146\5.\30\2\u0144\u0146")
        buf.write("\5\62\32\2\u0145\u0143\3\2\2\2\u0145\u0144\3\2\2\2\u0146")
        buf.write("C\3\2\2\2\u0147\u0148\7\21\2\2\u0148\u0149\7%\2\2\u0149")
        buf.write("\u014a\5X-\2\u014a\u014b\7&\2\2\u014b\u014c\5v<\2\u014c")
        buf.write("\u014d\5\64\33\2\u014dE\3\2\2\2\u014e\u014f\7\n\2\2\u014f")
        buf.write("\u0150\7/\2\2\u0150\u0151\7\13\2\2\u0151\u0152\5X-\2\u0152")
        buf.write("\u0153\7\f\2\2\u0153\u0154\5X-\2\u0154\u0155\5v<\2\u0155")
        buf.write("\u0156\5,\27\2\u0156G\3\2\2\2\u0157\u015a\7/\2\2\u0158")
        buf.write("\u015a\5p9\2\u0159\u0157\3\2\2\2\u0159\u0158\3\2\2\2\u015a")
        buf.write("\u015b\3\2\2\2\u015b\u015c\7\33\2\2\u015c\u015d\5X-\2")
        buf.write("\u015d\u015e\5t;\2\u015eI\3\2\2\2\u015f\u0160\7\b\2\2")
        buf.write("\u0160\u0161\5X-\2\u0161\u0162\5t;\2\u0162K\3\2\2\2\u0163")
        buf.write("\u0164\7\r\2\2\u0164\u0165\5t;\2\u0165M\3\2\2\2\u0166")
        buf.write("\u0167\7\16\2\2\u0167\u0168\5t;\2\u0168O\3\2\2\2\u0169")
        buf.write("\u016a\5R*\2\u016a\u016b\5t;\2\u016bQ\3\2\2\2\u016c\u016d")
        buf.write("\7/\2\2\u016d\u016e\7%\2\2\u016e\u016f\5T+\2\u016f\u0170")
        buf.write("\7&\2\2\u0170S\3\2\2\2\u0171\u0172\5X-\2\u0172\u0173\5")
        buf.write("V,\2\u0173\u0176\3\2\2\2\u0174\u0176\3\2\2\2\u0175\u0171")
        buf.write("\3\2\2\2\u0175\u0174\3\2\2\2\u0176U\3\2\2\2\u0177\u0178")
        buf.write("\7)\2\2\u0178\u0179\5X-\2\u0179\u017a\5V,\2\u017a\u017d")
        buf.write("\3\2\2\2\u017b\u017d\3\2\2\2\u017c\u0177\3\2\2\2\u017c")
        buf.write("\u017b\3\2\2\2\u017dW\3\2\2\2\u017e\u017f\5Z.\2\u017f")
        buf.write("\u0180\7 \2\2\u0180\u0181\5Z.\2\u0181\u0184\3\2\2\2\u0182")
        buf.write("\u0184\5Z.\2\u0183\u017e\3\2\2\2\u0183\u0182\3\2\2\2\u0184")
        buf.write("Y\3\2\2\2\u0185\u0186\5\\/\2\u0186\u0187\5j\66\2\u0187")
        buf.write("\u0188\5\\/\2\u0188\u018b\3\2\2\2\u0189\u018b\5\\/\2\u018a")
        buf.write("\u0185\3\2\2\2\u018a\u0189\3\2\2\2\u018b[\3\2\2\2\u018c")
        buf.write("\u018d\b/\1\2\u018d\u018e\5^\60\2\u018e\u0194\3\2\2\2")
        buf.write("\u018f\u0190\f\4\2\2\u0190\u0191\t\4\2\2\u0191\u0193\5")
        buf.write("^\60\2\u0192\u018f\3\2\2\2\u0193\u0196\3\2\2\2\u0194\u0192")
        buf.write("\3\2\2\2\u0194\u0195\3\2\2\2\u0195]\3\2\2\2\u0196\u0194")
        buf.write("\3\2\2\2\u0197\u0198\b\60\1\2\u0198\u0199\5`\61\2\u0199")
        buf.write("\u019f\3\2\2\2\u019a\u019b\f\4\2\2\u019b\u019c\t\5\2\2")
        buf.write("\u019c\u019e\5`\61\2\u019d\u019a\3\2\2\2\u019e\u01a1\3")
        buf.write("\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0_")
        buf.write("\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2\u01a3\b\61\1\2\u01a3")
        buf.write("\u01a4\5b\62\2\u01a4\u01aa\3\2\2\2\u01a5\u01a6\f\4\2\2")
        buf.write("\u01a6\u01a7\t\6\2\2\u01a7\u01a9\5b\62\2\u01a8\u01a5\3")
        buf.write("\2\2\2\u01a9\u01ac\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01ab")
        buf.write("\3\2\2\2\u01aba\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ad\u01ae")
        buf.write("\7\"\2\2\u01ae\u01b1\5b\62\2\u01af\u01b1\5d\63\2\u01b0")
        buf.write("\u01ad\3\2\2\2\u01b0\u01af\3\2\2\2\u01b1c\3\2\2\2\u01b2")
        buf.write("\u01b3\7\25\2\2\u01b3\u01b6\5d\63\2\u01b4\u01b6\5f\64")
        buf.write("\2\u01b5\u01b2\3\2\2\2\u01b5\u01b4\3\2\2\2\u01b6e\3\2")
        buf.write("\2\2\u01b7\u01bf\7+\2\2\u01b8\u01bf\7,\2\2\u01b9\u01bf")
        buf.write("\7-\2\2\u01ba\u01bf\7/\2\2\u01bb\u01bf\5l\67\2\u01bc\u01bf")
        buf.write("\5R*\2\u01bd\u01bf\5h\65\2\u01be\u01b7\3\2\2\2\u01be\u01b8")
        buf.write("\3\2\2\2\u01be\u01b9\3\2\2\2\u01be\u01ba\3\2\2\2\u01be")
        buf.write("\u01bb\3\2\2\2\u01be\u01bc\3\2\2\2\u01be\u01bd\3\2\2\2")
        buf.write("\u01bfg\3\2\2\2\u01c0\u01c1\7%\2\2\u01c1\u01c2\5X-\2\u01c2")
        buf.write("\u01c3\7&\2\2\u01c3i\3\2\2\2\u01c4\u01c5\t\7\2\2\u01c5")
        buf.write("k\3\2\2\2\u01c6\u01c9\7/\2\2\u01c7\u01c9\5R*\2\u01c8\u01c6")
        buf.write("\3\2\2\2\u01c8\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca")
        buf.write("\u01cb\7\'\2\2\u01cb\u01cc\5r:\2\u01cc\u01cd\7(\2\2\u01cd")
        buf.write("m\3\2\2\2\u01ce\u01cf\5R*\2\u01cf\u01d0\7\'\2\2\u01d0")
        buf.write("\u01d1\5r:\2\u01d1\u01d2\7(\2\2\u01d2o\3\2\2\2\u01d3\u01d4")
        buf.write("\7/\2\2\u01d4\u01d5\7\'\2\2\u01d5\u01d6\5r:\2\u01d6\u01d7")
        buf.write("\7(\2\2\u01d7q\3\2\2\2\u01d8\u01d9\5X-\2\u01d9\u01da\7")
        buf.write(")\2\2\u01da\u01db\5r:\2\u01db\u01de\3\2\2\2\u01dc\u01de")
        buf.write("\5X-\2\u01dd\u01d8\3\2\2\2\u01dd\u01dc\3\2\2\2\u01des")
        buf.write("\3\2\2\2\u01df\u01e0\7*\2\2\u01e0\u01e3\5t;\2\u01e1\u01e3")
        buf.write("\7*\2\2\u01e2\u01df\3\2\2\2\u01e2\u01e1\3\2\2\2\u01e3")
        buf.write("u\3\2\2\2\u01e4\u01e5\7*\2\2\u01e5\u01e8\5v<\2\u01e6\u01e8")
        buf.write("\3\2\2\2\u01e7\u01e4\3\2\2\2\u01e7\u01e6\3\2\2\2\u01e8")
        buf.write("w\3\2\2\2*\177\u0083\u0087\u008d\u0095\u00a1\u00ad\u00b4")
        buf.write("\u00bb\u00c6\u00d6\u00dd\u00e3\u00e7\u00ea\u00f6\u00fa")
        buf.write("\u0104\u0108\u0111\u0118\u0121\u0136\u013c\u0145\u0159")
        buf.write("\u0175\u017c\u0183\u018a\u0194\u019f\u01aa\u01b0\u01b5")
        buf.write("\u01be\u01c8\u01dd\u01e2\u01e7")
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
                      "COMMA", "NEWLINE", "NUMBER", "BOOLEAN", "STRING", 
                      "COMMENT", "IDENTIFIER", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                      "ERROR_CHAR" ]

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
    RULE_element_expression = 53
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
                   "element_expression", "function_extract_expression", 
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
    NUMBER=41
    BOOLEAN=42
    STRING=43
    COMMENT=44
    IDENTIFIER=45
    WS=46
    ILLEGAL_ESCAPE=47
    UNCLOSE_STRING=48
    ERROR_CHAR=49

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
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(ZCodeParser.RETURN)
            self.state = 350
            self.expression()
            self.state = 351
            self.newline_list()
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
            self.state = 353
            self.match(ZCodeParser.BREAK)
            self.state = 354
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
            self.state = 356
            self.match(ZCodeParser.CONTINUE)
            self.state = 357
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
            self.state = 359
            self.function_call()
            self.state = 360
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
            self.state = 362
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 363
            self.match(ZCodeParser.LEFT_PARENTHESIS)
            self.state = 364
            self.argument_list()
            self.state = 365
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
            self.state = 371
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS, ZCodeParser.NOT, ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.NUMBER, ZCodeParser.BOOLEAN, ZCodeParser.STRING, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.expression()
                self.state = 368
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
            self.state = 378
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.match(ZCodeParser.COMMA)
                self.state = 374
                self.expression()
                self.state = 375
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
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.expression1()
                self.state = 381
                self.match(ZCodeParser.STRING_CONCATENATION)
                self.state = 382
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
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
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.expression2(0)
                self.state = 388
                self.relational_operator()
                self.state = 389
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
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
            self.state = 395
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 402
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 397
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 398
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 399
                    self.expression3(0) 
                self.state = 404
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
            self.state = 406
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 413
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 408
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 409
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 410
                    self.expression4(0) 
                self.state = 415
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
            self.state = 417
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 424
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 419
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 420
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MULTIPLY) | (1 << ZCodeParser.DIVIDE) | (1 << ZCodeParser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 421
                    self.expression5() 
                self.state = 426
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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
            self.state = 430
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.match(ZCodeParser.NOT)
                self.state = 428
                self.expression5()
                pass
            elif token in [ZCodeParser.MINUS, ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.NUMBER, ZCodeParser.BOOLEAN, ZCodeParser.STRING, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
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
            self.state = 435
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                self.match(ZCodeParser.MINUS)
                self.state = 433
                self.expression6()
                pass
            elif token in [ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.NUMBER, ZCodeParser.BOOLEAN, ZCodeParser.STRING, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
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

        def element_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Element_expressionContext,0)


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
            self.state = 444
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
                self.match(ZCodeParser.BOOLEAN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 439
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 440
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 441
                self.element_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 442
                self.function_call()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 443
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
            self.state = 446
            self.match(ZCodeParser.LEFT_PARENTHESIS)
            self.state = 447
            self.expression()
            self.state = 448
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
            self.state = 450
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


    class Element_expressionContext(ParserRuleContext):
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
            return ZCodeParser.RULE_element_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_expression" ):
                return visitor.visitElement_expression(self)
            else:
                return visitor.visitChildren(self)




    def element_expression(self):

        localctx = ZCodeParser.Element_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_element_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 452
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 453
                self.function_call()
                pass


            self.state = 456
            self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
            self.state = 457
            self.index_operators()
            self.state = 458
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
            self.state = 460
            self.function_call()
            self.state = 461
            self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
            self.state = 462
            self.index_operators()
            self.state = 463
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
            self.state = 465
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 466
            self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
            self.state = 467
            self.index_operators()
            self.state = 468
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
            self.state = 475
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 470
                self.expression()
                self.state = 471
                self.match(ZCodeParser.COMMA)
                self.state = 472
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 474
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
            self.state = 480
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.match(ZCodeParser.NEWLINE)
                self.state = 478
                self.newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 479
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
            self.state = 485
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self.match(ZCodeParser.NEWLINE)
                self.state = 483
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
         




