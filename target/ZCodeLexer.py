# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *
2113376



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u0189\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3&")
        buf.write("\3&\3\'\3\'\3(\3(\3)\5)\u0105\n)\3)\3)\3*\3*\3*\7*\u010c")
        buf.write("\n*\f*\16*\u010f\13*\3*\3*\5*\u0113\n*\3*\3*\3+\3+\5+")
        buf.write("\u0119\n+\3+\5+\u011c\n+\3,\3,\3,\3,\3,\3,\3,\3,\3,\5")
        buf.write(",\u0127\n,\3-\3-\3-\7-\u012c\n-\f-\16-\u012f\13-\3-\3")
        buf.write("-\3-\3.\3.\3.\3.\7.\u0138\n.\f.\16.\u013b\13.\3.\5.\u013e")
        buf.write("\n.\3.\3.\5.\u0142\n.\3.\3.\3/\3/\7/\u0148\n/\f/\16/\u014b")
        buf.write("\13/\3\60\6\60\u014e\n\60\r\60\16\60\u014f\3\60\3\60\3")
        buf.write("\61\3\61\3\61\7\61\u0157\n\61\f\61\16\61\u015a\13\61\3")
        buf.write("\61\3\61\3\61\3\61\3\62\3\62\3\62\3\63\6\63\u0164\n\63")
        buf.write("\r\63\16\63\u0165\3\64\3\64\7\64\u016a\n\64\f\64\16\64")
        buf.write("\u016d\13\64\3\65\3\65\5\65\u0171\n\65\3\65\6\65\u0174")
        buf.write("\n\65\r\65\16\65\u0175\3\66\3\66\3\66\3\66\3\66\3\66\3")
        buf.write("\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\5\66")
        buf.write("\u0188\n\66\3\u0139\2\67\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\2g\2i\2k\2\3\2\n\6\2\f\f\17\17$$^^\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\5\2\n\13\16\16\"\"\t\2))^^ddhhppttvv\3\2\62;")
        buf.write("\4\2GGgg\4\2--//\2\u019f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\3m\3\2\2\2\5t\3\2\2\2\7y\3\2\2\2\t\u0080\3\2")
        buf.write("\2\2\13\u0084\3\2\2\2\r\u008c\3\2\2\2\17\u0093\3\2\2\2")
        buf.write("\21\u0098\3\2\2\2\23\u009c\3\2\2\2\25\u00a2\3\2\2\2\27")
        buf.write("\u00a5\3\2\2\2\31\u00ab\3\2\2\2\33\u00b4\3\2\2\2\35\u00b7")
        buf.write("\3\2\2\2\37\u00bc\3\2\2\2!\u00c1\3\2\2\2#\u00c7\3\2\2")
        buf.write("\2%\u00cb\3\2\2\2\'\u00cd\3\2\2\2)\u00cf\3\2\2\2+\u00d1")
        buf.write("\3\2\2\2-\u00d3\3\2\2\2/\u00d5\3\2\2\2\61\u00d7\3\2\2")
        buf.write("\2\63\u00da\3\2\2\2\65\u00dd\3\2\2\2\67\u00df\3\2\2\2")
        buf.write("9\u00e2\3\2\2\2;\u00e4\3\2\2\2=\u00e7\3\2\2\2?\u00eb\3")
        buf.write("\2\2\2A\u00ee\3\2\2\2C\u00f2\3\2\2\2E\u00f6\3\2\2\2G\u00f9")
        buf.write("\3\2\2\2I\u00fb\3\2\2\2K\u00fd\3\2\2\2M\u00ff\3\2\2\2")
        buf.write("O\u0101\3\2\2\2Q\u0104\3\2\2\2S\u0108\3\2\2\2U\u0116\3")
        buf.write("\2\2\2W\u0126\3\2\2\2Y\u0128\3\2\2\2[\u0133\3\2\2\2]\u0145")
        buf.write("\3\2\2\2_\u014d\3\2\2\2a\u0153\3\2\2\2c\u015f\3\2\2\2")
        buf.write("e\u0163\3\2\2\2g\u0167\3\2\2\2i\u016e\3\2\2\2k\u0187\3")
        buf.write("\2\2\2mn\7p\2\2no\7w\2\2op\7o\2\2pq\7d\2\2qr\7g\2\2rs")
        buf.write("\7t\2\2s\4\3\2\2\2tu\7d\2\2uv\7q\2\2vw\7q\2\2wx\7n\2\2")
        buf.write("x\6\3\2\2\2yz\7u\2\2z{\7v\2\2{|\7t\2\2|}\7k\2\2}~\7p\2")
        buf.write("\2~\177\7i\2\2\177\b\3\2\2\2\u0080\u0081\7x\2\2\u0081")
        buf.write("\u0082\7c\2\2\u0082\u0083\7t\2\2\u0083\n\3\2\2\2\u0084")
        buf.write("\u0085\7f\2\2\u0085\u0086\7{\2\2\u0086\u0087\7p\2\2\u0087")
        buf.write("\u0088\7c\2\2\u0088\u0089\7o\2\2\u0089\u008a\7k\2\2\u008a")
        buf.write("\u008b\7e\2\2\u008b\f\3\2\2\2\u008c\u008d\7t\2\2\u008d")
        buf.write("\u008e\7g\2\2\u008e\u008f\7v\2\2\u008f\u0090\7w\2\2\u0090")
        buf.write("\u0091\7t\2\2\u0091\u0092\7p\2\2\u0092\16\3\2\2\2\u0093")
        buf.write("\u0094\7h\2\2\u0094\u0095\7w\2\2\u0095\u0096\7p\2\2\u0096")
        buf.write("\u0097\7e\2\2\u0097\20\3\2\2\2\u0098\u0099\7h\2\2\u0099")
        buf.write("\u009a\7q\2\2\u009a\u009b\7t\2\2\u009b\22\3\2\2\2\u009c")
        buf.write("\u009d\7w\2\2\u009d\u009e\7p\2\2\u009e\u009f\7v\2\2\u009f")
        buf.write("\u00a0\7k\2\2\u00a0\u00a1\7n\2\2\u00a1\24\3\2\2\2\u00a2")
        buf.write("\u00a3\7d\2\2\u00a3\u00a4\7{\2\2\u00a4\26\3\2\2\2\u00a5")
        buf.write("\u00a6\7d\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8\7g\2\2\u00a8")
        buf.write("\u00a9\7c\2\2\u00a9\u00aa\7m\2\2\u00aa\30\3\2\2\2\u00ab")
        buf.write("\u00ac\7e\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae\7p\2\2\u00ae")
        buf.write("\u00af\7v\2\2\u00af\u00b0\7k\2\2\u00b0\u00b1\7p\2\2\u00b1")
        buf.write("\u00b2\7w\2\2\u00b2\u00b3\7g\2\2\u00b3\32\3\2\2\2\u00b4")
        buf.write("\u00b5\7k\2\2\u00b5\u00b6\7h\2\2\u00b6\34\3\2\2\2\u00b7")
        buf.write("\u00b8\7g\2\2\u00b8\u00b9\7n\2\2\u00b9\u00ba\7u\2\2\u00ba")
        buf.write("\u00bb\7g\2\2\u00bb\36\3\2\2\2\u00bc\u00bd\7g\2\2\u00bd")
        buf.write("\u00be\7n\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0\7h\2\2\u00c0")
        buf.write(" \3\2\2\2\u00c1\u00c2\7d\2\2\u00c2\u00c3\7g\2\2\u00c3")
        buf.write("\u00c4\7i\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6\7p\2\2\u00c6")
        buf.write("\"\3\2\2\2\u00c7\u00c8\7g\2\2\u00c8\u00c9\7p\2\2\u00c9")
        buf.write("\u00ca\7f\2\2\u00ca$\3\2\2\2\u00cb\u00cc\7-\2\2\u00cc")
        buf.write("&\3\2\2\2\u00cd\u00ce\7/\2\2\u00ce(\3\2\2\2\u00cf\u00d0")
        buf.write("\7,\2\2\u00d0*\3\2\2\2\u00d1\u00d2\7\61\2\2\u00d2,\3\2")
        buf.write("\2\2\u00d3\u00d4\7\'\2\2\u00d4.\3\2\2\2\u00d5\u00d6\7")
        buf.write("?\2\2\u00d6\60\3\2\2\2\u00d7\u00d8\7#\2\2\u00d8\u00d9")
        buf.write("\7?\2\2\u00d9\62\3\2\2\2\u00da\u00db\7>\2\2\u00db\u00dc")
        buf.write("\7/\2\2\u00dc\64\3\2\2\2\u00dd\u00de\7>\2\2\u00de\66\3")
        buf.write("\2\2\2\u00df\u00e0\7>\2\2\u00e0\u00e1\7?\2\2\u00e18\3")
        buf.write("\2\2\2\u00e2\u00e3\7@\2\2\u00e3:\3\2\2\2\u00e4\u00e5\7")
        buf.write("@\2\2\u00e5\u00e6\7?\2\2\u00e6<\3\2\2\2\u00e7\u00e8\7")
        buf.write("\60\2\2\u00e8\u00e9\7\60\2\2\u00e9\u00ea\7\60\2\2\u00ea")
        buf.write(">\3\2\2\2\u00eb\u00ec\7?\2\2\u00ec\u00ed\7?\2\2\u00ed")
        buf.write("@\3\2\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0\7q\2\2\u00f0")
        buf.write("\u00f1\7v\2\2\u00f1B\3\2\2\2\u00f2\u00f3\7c\2\2\u00f3")
        buf.write("\u00f4\7p\2\2\u00f4\u00f5\7f\2\2\u00f5D\3\2\2\2\u00f6")
        buf.write("\u00f7\7q\2\2\u00f7\u00f8\7t\2\2\u00f8F\3\2\2\2\u00f9")
        buf.write("\u00fa\7*\2\2\u00faH\3\2\2\2\u00fb\u00fc\7+\2\2\u00fc")
        buf.write("J\3\2\2\2\u00fd\u00fe\7]\2\2\u00feL\3\2\2\2\u00ff\u0100")
        buf.write("\7_\2\2\u0100N\3\2\2\2\u0101\u0102\7.\2\2\u0102P\3\2\2")
        buf.write("\2\u0103\u0105\7\17\2\2\u0104\u0103\3\2\2\2\u0104\u0105")
        buf.write("\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0107\7\f\2\2\u0107")
        buf.write("R\3\2\2\2\u0108\u010d\7$\2\2\u0109\u010c\5k\66\2\u010a")
        buf.write("\u010c\n\2\2\2\u010b\u0109\3\2\2\2\u010b\u010a\3\2\2\2")
        buf.write("\u010c\u010f\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010e\3")
        buf.write("\2\2\2\u010e\u0112\3\2\2\2\u010f\u010d\3\2\2\2\u0110\u0111")
        buf.write("\7)\2\2\u0111\u0113\7$\2\2\u0112\u0110\3\2\2\2\u0112\u0113")
        buf.write("\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0115\b*\2\2\u0115")
        buf.write("T\3\2\2\2\u0116\u0118\5e\63\2\u0117\u0119\5g\64\2\u0118")
        buf.write("\u0117\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011b\3\2\2\2")
        buf.write("\u011a\u011c\5i\65\2\u011b\u011a\3\2\2\2\u011b\u011c\3")
        buf.write("\2\2\2\u011cV\3\2\2\2\u011d\u011e\7v\2\2\u011e\u011f\7")
        buf.write("t\2\2\u011f\u0120\7w\2\2\u0120\u0127\7g\2\2\u0121\u0122")
        buf.write("\7h\2\2\u0122\u0123\7c\2\2\u0123\u0124\7n\2\2\u0124\u0125")
        buf.write("\7u\2\2\u0125\u0127\7g\2\2\u0126\u011d\3\2\2\2\u0126\u0121")
        buf.write("\3\2\2\2\u0127X\3\2\2\2\u0128\u012d\7$\2\2\u0129\u012c")
        buf.write("\5k\66\2\u012a\u012c\n\2\2\2\u012b\u0129\3\2\2\2\u012b")
        buf.write("\u012a\3\2\2\2\u012c\u012f\3\2\2\2\u012d\u012b\3\2\2\2")
        buf.write("\u012d\u012e\3\2\2\2\u012e\u0130\3\2\2\2\u012f\u012d\3")
        buf.write("\2\2\2\u0130\u0131\7$\2\2\u0131\u0132\b-\3\2\u0132Z\3")
        buf.write("\2\2\2\u0133\u0134\7%\2\2\u0134\u0135\7%\2\2\u0135\u0139")
        buf.write("\3\2\2\2\u0136\u0138\13\2\2\2\u0137\u0136\3\2\2\2\u0138")
        buf.write("\u013b\3\2\2\2\u0139\u013a\3\2\2\2\u0139\u0137\3\2\2\2")
        buf.write("\u013a\u0141\3\2\2\2\u013b\u0139\3\2\2\2\u013c\u013e\7")
        buf.write("\17\2\2\u013d\u013c\3\2\2\2\u013d\u013e\3\2\2\2\u013e")
        buf.write("\u013f\3\2\2\2\u013f\u0142\7\f\2\2\u0140\u0142\7\2\2\3")
        buf.write("\u0141\u013d\3\2\2\2\u0141\u0140\3\2\2\2\u0142\u0143\3")
        buf.write("\2\2\2\u0143\u0144\b.\4\2\u0144\\\3\2\2\2\u0145\u0149")
        buf.write("\t\3\2\2\u0146\u0148\t\4\2\2\u0147\u0146\3\2\2\2\u0148")
        buf.write("\u014b\3\2\2\2\u0149\u0147\3\2\2\2\u0149\u014a\3\2\2\2")
        buf.write("\u014a^\3\2\2\2\u014b\u0149\3\2\2\2\u014c\u014e\t\5\2")
        buf.write("\2\u014d\u014c\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u014d")
        buf.write("\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0151\3\2\2\2\u0151")
        buf.write("\u0152\b\60\4\2\u0152`\3\2\2\2\u0153\u0158\7$\2\2\u0154")
        buf.write("\u0157\5k\66\2\u0155\u0157\n\2\2\2\u0156\u0154\3\2\2\2")
        buf.write("\u0156\u0155\3\2\2\2\u0157\u015a\3\2\2\2\u0158\u0156\3")
        buf.write("\2\2\2\u0158\u0159\3\2\2\2\u0159\u015b\3\2\2\2\u015a\u0158")
        buf.write("\3\2\2\2\u015b\u015c\7^\2\2\u015c\u015d\n\6\2\2\u015d")
        buf.write("\u015e\b\61\5\2\u015eb\3\2\2\2\u015f\u0160\13\2\2\2\u0160")
        buf.write("\u0161\b\62\6\2\u0161d\3\2\2\2\u0162\u0164\t\7\2\2\u0163")
        buf.write("\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0163\3\2\2\2")
        buf.write("\u0165\u0166\3\2\2\2\u0166f\3\2\2\2\u0167\u016b\13\2\2")
        buf.write("\2\u0168\u016a\t\7\2\2\u0169\u0168\3\2\2\2\u016a\u016d")
        buf.write("\3\2\2\2\u016b\u0169\3\2\2\2\u016b\u016c\3\2\2\2\u016c")
        buf.write("h\3\2\2\2\u016d\u016b\3\2\2\2\u016e\u0170\t\b\2\2\u016f")
        buf.write("\u0171\t\t\2\2\u0170\u016f\3\2\2\2\u0170\u0171\3\2\2\2")
        buf.write("\u0171\u0173\3\2\2\2\u0172\u0174\t\7\2\2\u0173\u0172\3")
        buf.write("\2\2\2\u0174\u0175\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176")
        buf.write("\3\2\2\2\u0176j\3\2\2\2\u0177\u0178\7^\2\2\u0178\u0188")
        buf.write("\7d\2\2\u0179\u017a\7^\2\2\u017a\u0188\7h\2\2\u017b\u017c")
        buf.write("\7^\2\2\u017c\u0188\7t\2\2\u017d\u017e\7^\2\2\u017e\u0188")
        buf.write("\7p\2\2\u017f\u0180\7^\2\2\u0180\u0188\7v\2\2\u0181\u0182")
        buf.write("\7^\2\2\u0182\u0188\7)\2\2\u0183\u0184\7^\2\2\u0184\u0188")
        buf.write("\7^\2\2\u0185\u0186\7)\2\2\u0186\u0188\7$\2\2\u0187\u0177")
        buf.write("\3\2\2\2\u0187\u0179\3\2\2\2\u0187\u017b\3\2\2\2\u0187")
        buf.write("\u017d\3\2\2\2\u0187\u017f\3\2\2\2\u0187\u0181\3\2\2\2")
        buf.write("\u0187\u0183\3\2\2\2\u0187\u0185\3\2\2\2\u0188l\3\2\2")
        buf.write("\2\30\2\u0104\u010b\u010d\u0112\u0118\u011b\u0126\u012b")
        buf.write("\u012d\u0139\u013d\u0141\u0149\u014f\u0156\u0158\u0165")
        buf.write("\u016b\u0170\u0175\u0187\7\3*\2\3-\3\b\2\2\3\61\4\3\62")
        buf.write("\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TYPE_NUMBER = 1
    TYPE_BOOL = 2
    TYPE_STRING = 3
    VAR = 4
    DYNAMIC = 5
    RETURN = 6
    FUNCTION = 7
    FOR = 8
    UNTIL = 9
    BY = 10
    BREAK = 11
    CONTINUE = 12
    IF = 13
    ELSE = 14
    ELIF = 15
    BEGIN = 16
    END = 17
    PLUS = 18
    MINUS = 19
    MULTIPLY = 20
    DIVIDE = 21
    MODULO = 22
    EQUAL = 23
    NOT_EQUAL = 24
    ASSIGNMENT = 25
    LESS_THAN = 26
    LESS_THAN_OR_EQUAL = 27
    GREATER_THAN = 28
    GREATER_THAN_OR_EQUAL = 29
    STRING_CONCATENATION = 30
    STRING_COMPARISION = 31
    NOT = 32
    AND = 33
    OR = 34
    LEFT_PARENTHESIS = 35
    RIGHT_PARENTHESIS = 36
    LEFT_SQUARE_BRACKET = 37
    RIGHT_SQUARE_BRACKET = 38
    COMMA = 39
    NEWLINE = 40
    UNCLOSE_STRING = 41
    NUMBER = 42
    BOOLEAN = 43
    STRING = 44
    COMMENT = 45
    IDENTIFIER = 46
    WS = 47
    ILLEGAL_ESCAPE = 48
    ERROR_TOKEN = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'number'", "'bool'", "'string'", "'var'", "'dynamic'", "'return'", 
            "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
            "'if'", "'else'", "'elif'", "'begin'", "'end'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'='", "'!='", "'<-'", "'<'", "'<='", "'>'", 
            "'>='", "'...'", "'=='", "'not'", "'and'", "'or'", "'('", "')'", 
            "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "TYPE_NUMBER", "TYPE_BOOL", "TYPE_STRING", "VAR", "DYNAMIC", 
            "RETURN", "FUNCTION", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "PLUS", "MINUS", "MULTIPLY", 
            "DIVIDE", "MODULO", "EQUAL", "NOT_EQUAL", "ASSIGNMENT", "LESS_THAN", 
            "LESS_THAN_OR_EQUAL", "GREATER_THAN", "GREATER_THAN_OR_EQUAL", 
            "STRING_CONCATENATION", "STRING_COMPARISION", "NOT", "AND", 
            "OR", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", "LEFT_SQUARE_BRACKET", 
            "RIGHT_SQUARE_BRACKET", "COMMA", "NEWLINE", "UNCLOSE_STRING", 
            "NUMBER", "BOOLEAN", "STRING", "COMMENT", "IDENTIFIER", "WS", 
            "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    ruleNames = [ "TYPE_NUMBER", "TYPE_BOOL", "TYPE_STRING", "VAR", "DYNAMIC", 
                  "RETURN", "FUNCTION", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
                  "IF", "ELSE", "ELIF", "BEGIN", "END", "PLUS", "MINUS", 
                  "MULTIPLY", "DIVIDE", "MODULO", "EQUAL", "NOT_EQUAL", 
                  "ASSIGNMENT", "LESS_THAN", "LESS_THAN_OR_EQUAL", "GREATER_THAN", 
                  "GREATER_THAN_OR_EQUAL", "STRING_CONCATENATION", "STRING_COMPARISION", 
                  "NOT", "AND", "OR", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", 
                  "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", "COMMA", 
                  "NEWLINE", "UNCLOSE_STRING", "NUMBER", "BOOLEAN", "STRING", 
                  "COMMENT", "IDENTIFIER", "WS", "ILLEGAL_ESCAPE", "ERROR_TOKEN", 
                  "INTEGER", "DECIMAL", "EXPONENT", "ESCAPE_SEQUENCE" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[40] = self.UNCLOSE_STRING_action 
            actions[43] = self.STRING_action 
            actions[47] = self.ILLEGAL_ESCAPE_action 
            actions[48] = self.ERROR_TOKEN_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise UncloseString(self.text[1:])
     

    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text[1:-1]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


