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
        buf.write("\u0185\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3&\3\'\3\'\3(\3(\3)\5)\u0105\n)\3)\3)\3*\3*\5*\u010b")
        buf.write("\n*\3*\5*\u010e\n*\3+\3+\3+\3+\3+\3+\3+\3+\3+\5+\u0119")
        buf.write("\n+\3,\3,\3,\7,\u011e\n,\f,\16,\u0121\13,\3,\3,\3,\3-")
        buf.write("\3-\3-\3-\7-\u012a\n-\f-\16-\u012d\13-\3-\5-\u0130\n-")
        buf.write("\3-\3-\5-\u0134\n-\3-\3-\3.\3.\7.\u013a\n.\f.\16.\u013d")
        buf.write("\13.\3/\6/\u0140\n/\r/\16/\u0141\3/\3/\3\60\3\60\3\60")
        buf.write("\7\60\u0149\n\60\f\60\16\60\u014c\13\60\3\60\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\7\61\u0155\n\61\f\61\16\61\u0158")
        buf.write("\13\61\3\61\3\61\3\62\3\62\3\62\3\63\6\63\u0160\n\63\r")
        buf.write("\63\16\63\u0161\3\64\3\64\7\64\u0166\n\64\f\64\16\64\u0169")
        buf.write("\13\64\3\65\3\65\5\65\u016d\n\65\3\65\6\65\u0170\n\65")
        buf.write("\r\65\16\65\u0171\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3")
        buf.write("\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u0184")
        buf.write("\n\66\3\u012b\2\67\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ")
        buf.write("?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\2g\2")
        buf.write("i\2k\2\3\2\n\6\2\f\f\17\17$$^^\5\2C\\aac|\6\2\62;C\\a")
        buf.write("ac|\5\2\n\13\16\16\"\"\t\2))^^ddhhppttvv\3\2\62;\4\2G")
        buf.write("Ggg\4\2--//\2\u019a\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\3m\3\2\2\2\5t\3\2\2\2\7y\3\2\2\2\t\u0080\3\2\2\2\13")
        buf.write("\u0084\3\2\2\2\r\u008c\3\2\2\2\17\u0093\3\2\2\2\21\u0098")
        buf.write("\3\2\2\2\23\u009c\3\2\2\2\25\u00a2\3\2\2\2\27\u00a5\3")
        buf.write("\2\2\2\31\u00ab\3\2\2\2\33\u00b4\3\2\2\2\35\u00b7\3\2")
        buf.write("\2\2\37\u00bc\3\2\2\2!\u00c1\3\2\2\2#\u00c7\3\2\2\2%\u00cb")
        buf.write("\3\2\2\2\'\u00cd\3\2\2\2)\u00cf\3\2\2\2+\u00d1\3\2\2\2")
        buf.write("-\u00d3\3\2\2\2/\u00d5\3\2\2\2\61\u00d7\3\2\2\2\63\u00da")
        buf.write("\3\2\2\2\65\u00dd\3\2\2\2\67\u00df\3\2\2\29\u00e2\3\2")
        buf.write("\2\2;\u00e4\3\2\2\2=\u00e7\3\2\2\2?\u00eb\3\2\2\2A\u00ee")
        buf.write("\3\2\2\2C\u00f2\3\2\2\2E\u00f6\3\2\2\2G\u00f9\3\2\2\2")
        buf.write("I\u00fb\3\2\2\2K\u00fd\3\2\2\2M\u00ff\3\2\2\2O\u0101\3")
        buf.write("\2\2\2Q\u0104\3\2\2\2S\u0108\3\2\2\2U\u0118\3\2\2\2W\u011a")
        buf.write("\3\2\2\2Y\u0125\3\2\2\2[\u0137\3\2\2\2]\u013f\3\2\2\2")
        buf.write("_\u0145\3\2\2\2a\u0151\3\2\2\2c\u015b\3\2\2\2e\u015f\3")
        buf.write("\2\2\2g\u0163\3\2\2\2i\u016a\3\2\2\2k\u0183\3\2\2\2mn")
        buf.write("\7p\2\2no\7w\2\2op\7o\2\2pq\7d\2\2qr\7g\2\2rs\7t\2\2s")
        buf.write("\4\3\2\2\2tu\7d\2\2uv\7q\2\2vw\7q\2\2wx\7n\2\2x\6\3\2")
        buf.write("\2\2yz\7u\2\2z{\7v\2\2{|\7t\2\2|}\7k\2\2}~\7p\2\2~\177")
        buf.write("\7i\2\2\177\b\3\2\2\2\u0080\u0081\7x\2\2\u0081\u0082\7")
        buf.write("c\2\2\u0082\u0083\7t\2\2\u0083\n\3\2\2\2\u0084\u0085\7")
        buf.write("f\2\2\u0085\u0086\7{\2\2\u0086\u0087\7p\2\2\u0087\u0088")
        buf.write("\7c\2\2\u0088\u0089\7o\2\2\u0089\u008a\7k\2\2\u008a\u008b")
        buf.write("\7e\2\2\u008b\f\3\2\2\2\u008c\u008d\7t\2\2\u008d\u008e")
        buf.write("\7g\2\2\u008e\u008f\7v\2\2\u008f\u0090\7w\2\2\u0090\u0091")
        buf.write("\7t\2\2\u0091\u0092\7p\2\2\u0092\16\3\2\2\2\u0093\u0094")
        buf.write("\7h\2\2\u0094\u0095\7w\2\2\u0095\u0096\7p\2\2\u0096\u0097")
        buf.write("\7e\2\2\u0097\20\3\2\2\2\u0098\u0099\7h\2\2\u0099\u009a")
        buf.write("\7q\2\2\u009a\u009b\7t\2\2\u009b\22\3\2\2\2\u009c\u009d")
        buf.write("\7w\2\2\u009d\u009e\7p\2\2\u009e\u009f\7v\2\2\u009f\u00a0")
        buf.write("\7k\2\2\u00a0\u00a1\7n\2\2\u00a1\24\3\2\2\2\u00a2\u00a3")
        buf.write("\7d\2\2\u00a3\u00a4\7{\2\2\u00a4\26\3\2\2\2\u00a5\u00a6")
        buf.write("\7d\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9")
        buf.write("\7c\2\2\u00a9\u00aa\7m\2\2\u00aa\30\3\2\2\2\u00ab\u00ac")
        buf.write("\7e\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae\7p\2\2\u00ae\u00af")
        buf.write("\7v\2\2\u00af\u00b0\7k\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2")
        buf.write("\7w\2\2\u00b2\u00b3\7g\2\2\u00b3\32\3\2\2\2\u00b4\u00b5")
        buf.write("\7k\2\2\u00b5\u00b6\7h\2\2\u00b6\34\3\2\2\2\u00b7\u00b8")
        buf.write("\7g\2\2\u00b8\u00b9\7n\2\2\u00b9\u00ba\7u\2\2\u00ba\u00bb")
        buf.write("\7g\2\2\u00bb\36\3\2\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be")
        buf.write("\7n\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0\7h\2\2\u00c0 \3")
        buf.write("\2\2\2\u00c1\u00c2\7d\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4")
        buf.write("\7i\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6\7p\2\2\u00c6\"")
        buf.write("\3\2\2\2\u00c7\u00c8\7g\2\2\u00c8\u00c9\7p\2\2\u00c9\u00ca")
        buf.write("\7f\2\2\u00ca$\3\2\2\2\u00cb\u00cc\7-\2\2\u00cc&\3\2\2")
        buf.write("\2\u00cd\u00ce\7/\2\2\u00ce(\3\2\2\2\u00cf\u00d0\7,\2")
        buf.write("\2\u00d0*\3\2\2\2\u00d1\u00d2\7\61\2\2\u00d2,\3\2\2\2")
        buf.write("\u00d3\u00d4\7\'\2\2\u00d4.\3\2\2\2\u00d5\u00d6\7?\2\2")
        buf.write("\u00d6\60\3\2\2\2\u00d7\u00d8\7#\2\2\u00d8\u00d9\7?\2")
        buf.write("\2\u00d9\62\3\2\2\2\u00da\u00db\7>\2\2\u00db\u00dc\7/")
        buf.write("\2\2\u00dc\64\3\2\2\2\u00dd\u00de\7>\2\2\u00de\66\3\2")
        buf.write("\2\2\u00df\u00e0\7>\2\2\u00e0\u00e1\7?\2\2\u00e18\3\2")
        buf.write("\2\2\u00e2\u00e3\7@\2\2\u00e3:\3\2\2\2\u00e4\u00e5\7@")
        buf.write("\2\2\u00e5\u00e6\7?\2\2\u00e6<\3\2\2\2\u00e7\u00e8\7\60")
        buf.write("\2\2\u00e8\u00e9\7\60\2\2\u00e9\u00ea\7\60\2\2\u00ea>")
        buf.write("\3\2\2\2\u00eb\u00ec\7?\2\2\u00ec\u00ed\7?\2\2\u00ed@")
        buf.write("\3\2\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1")
        buf.write("\7v\2\2\u00f1B\3\2\2\2\u00f2\u00f3\7c\2\2\u00f3\u00f4")
        buf.write("\7p\2\2\u00f4\u00f5\7f\2\2\u00f5D\3\2\2\2\u00f6\u00f7")
        buf.write("\7q\2\2\u00f7\u00f8\7t\2\2\u00f8F\3\2\2\2\u00f9\u00fa")
        buf.write("\7*\2\2\u00faH\3\2\2\2\u00fb\u00fc\7+\2\2\u00fcJ\3\2\2")
        buf.write("\2\u00fd\u00fe\7]\2\2\u00feL\3\2\2\2\u00ff\u0100\7_\2")
        buf.write("\2\u0100N\3\2\2\2\u0101\u0102\7.\2\2\u0102P\3\2\2\2\u0103")
        buf.write("\u0105\7\17\2\2\u0104\u0103\3\2\2\2\u0104\u0105\3\2\2")
        buf.write("\2\u0105\u0106\3\2\2\2\u0106\u0107\7\f\2\2\u0107R\3\2")
        buf.write("\2\2\u0108\u010a\5e\63\2\u0109\u010b\5g\64\2\u010a\u0109")
        buf.write("\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u010d\3\2\2\2\u010c")
        buf.write("\u010e\5i\65\2\u010d\u010c\3\2\2\2\u010d\u010e\3\2\2\2")
        buf.write("\u010eT\3\2\2\2\u010f\u0110\7v\2\2\u0110\u0111\7t\2\2")
        buf.write("\u0111\u0112\7w\2\2\u0112\u0119\7g\2\2\u0113\u0114\7h")
        buf.write("\2\2\u0114\u0115\7c\2\2\u0115\u0116\7n\2\2\u0116\u0117")
        buf.write("\7u\2\2\u0117\u0119\7g\2\2\u0118\u010f\3\2\2\2\u0118\u0113")
        buf.write("\3\2\2\2\u0119V\3\2\2\2\u011a\u011f\7$\2\2\u011b\u011e")
        buf.write("\5k\66\2\u011c\u011e\n\2\2\2\u011d\u011b\3\2\2\2\u011d")
        buf.write("\u011c\3\2\2\2\u011e\u0121\3\2\2\2\u011f\u011d\3\2\2\2")
        buf.write("\u011f\u0120\3\2\2\2\u0120\u0122\3\2\2\2\u0121\u011f\3")
        buf.write("\2\2\2\u0122\u0123\7$\2\2\u0123\u0124\b,\2\2\u0124X\3")
        buf.write("\2\2\2\u0125\u0126\7%\2\2\u0126\u0127\7%\2\2\u0127\u012b")
        buf.write("\3\2\2\2\u0128\u012a\13\2\2\2\u0129\u0128\3\2\2\2\u012a")
        buf.write("\u012d\3\2\2\2\u012b\u012c\3\2\2\2\u012b\u0129\3\2\2\2")
        buf.write("\u012c\u0133\3\2\2\2\u012d\u012b\3\2\2\2\u012e\u0130\7")
        buf.write("\17\2\2\u012f\u012e\3\2\2\2\u012f\u0130\3\2\2\2\u0130")
        buf.write("\u0131\3\2\2\2\u0131\u0134\7\f\2\2\u0132\u0134\7\2\2\3")
        buf.write("\u0133\u012f\3\2\2\2\u0133\u0132\3\2\2\2\u0134\u0135\3")
        buf.write("\2\2\2\u0135\u0136\b-\3\2\u0136Z\3\2\2\2\u0137\u013b\t")
        buf.write("\3\2\2\u0138\u013a\t\4\2\2\u0139\u0138\3\2\2\2\u013a\u013d")
        buf.write("\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c")
        buf.write("\\\3\2\2\2\u013d\u013b\3\2\2\2\u013e\u0140\t\5\2\2\u013f")
        buf.write("\u013e\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u013f\3\2\2\2")
        buf.write("\u0141\u0142\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0144\b")
        buf.write("/\3\2\u0144^\3\2\2\2\u0145\u014a\7$\2\2\u0146\u0149\5")
        buf.write("k\66\2\u0147\u0149\n\2\2\2\u0148\u0146\3\2\2\2\u0148\u0147")
        buf.write("\3\2\2\2\u0149\u014c\3\2\2\2\u014a\u0148\3\2\2\2\u014a")
        buf.write("\u014b\3\2\2\2\u014b\u014d\3\2\2\2\u014c\u014a\3\2\2\2")
        buf.write("\u014d\u014e\7^\2\2\u014e\u014f\n\6\2\2\u014f\u0150\b")
        buf.write("\60\4\2\u0150`\3\2\2\2\u0151\u0156\7$\2\2\u0152\u0155")
        buf.write("\5k\66\2\u0153\u0155\n\2\2\2\u0154\u0152\3\2\2\2\u0154")
        buf.write("\u0153\3\2\2\2\u0155\u0158\3\2\2\2\u0156\u0154\3\2\2\2")
        buf.write("\u0156\u0157\3\2\2\2\u0157\u0159\3\2\2\2\u0158\u0156\3")
        buf.write("\2\2\2\u0159\u015a\b\61\5\2\u015ab\3\2\2\2\u015b\u015c")
        buf.write("\13\2\2\2\u015c\u015d\b\62\6\2\u015dd\3\2\2\2\u015e\u0160")
        buf.write("\t\7\2\2\u015f\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161")
        buf.write("\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162f\3\2\2\2\u0163")
        buf.write("\u0167\13\2\2\2\u0164\u0166\t\7\2\2\u0165\u0164\3\2\2")
        buf.write("\2\u0166\u0169\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168")
        buf.write("\3\2\2\2\u0168h\3\2\2\2\u0169\u0167\3\2\2\2\u016a\u016c")
        buf.write("\t\b\2\2\u016b\u016d\t\t\2\2\u016c\u016b\3\2\2\2\u016c")
        buf.write("\u016d\3\2\2\2\u016d\u016f\3\2\2\2\u016e\u0170\t\7\2\2")
        buf.write("\u016f\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u016f\3")
        buf.write("\2\2\2\u0171\u0172\3\2\2\2\u0172j\3\2\2\2\u0173\u0174")
        buf.write("\7^\2\2\u0174\u0184\7d\2\2\u0175\u0176\7^\2\2\u0176\u0184")
        buf.write("\7h\2\2\u0177\u0178\7^\2\2\u0178\u0184\7t\2\2\u0179\u017a")
        buf.write("\7^\2\2\u017a\u0184\7p\2\2\u017b\u017c\7^\2\2\u017c\u0184")
        buf.write("\7v\2\2\u017d\u017e\7^\2\2\u017e\u0184\7)\2\2\u017f\u0180")
        buf.write("\7^\2\2\u0180\u0184\7^\2\2\u0181\u0182\7)\2\2\u0182\u0184")
        buf.write("\7$\2\2\u0183\u0173\3\2\2\2\u0183\u0175\3\2\2\2\u0183")
        buf.write("\u0177\3\2\2\2\u0183\u0179\3\2\2\2\u0183\u017b\3\2\2\2")
        buf.write("\u0183\u017d\3\2\2\2\u0183\u017f\3\2\2\2\u0183\u0181\3")
        buf.write("\2\2\2\u0184l\3\2\2\2\27\2\u0104\u010a\u010d\u0118\u011d")
        buf.write("\u011f\u012b\u012f\u0133\u013b\u0141\u0148\u014a\u0154")
        buf.write("\u0156\u0161\u0167\u016c\u0171\u0183\7\3,\2\b\2\2\3\60")
        buf.write("\3\3\61\4\3\62\5")
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
    NUMBER = 41
    BOOLEAN = 42
    STRING = 43
    COMMENT = 44
    IDENTIFIER = 45
    WS = 46
    ILLEGAL_ESCAPE = 47
    UNCLOSE_STRING = 48
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
            "RIGHT_SQUARE_BRACKET", "COMMA", "NEWLINE", "NUMBER", "BOOLEAN", 
            "STRING", "COMMENT", "IDENTIFIER", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "ERROR_TOKEN" ]

    ruleNames = [ "TYPE_NUMBER", "TYPE_BOOL", "TYPE_STRING", "VAR", "DYNAMIC", 
                  "RETURN", "FUNCTION", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
                  "IF", "ELSE", "ELIF", "BEGIN", "END", "PLUS", "MINUS", 
                  "MULTIPLY", "DIVIDE", "MODULO", "EQUAL", "NOT_EQUAL", 
                  "ASSIGNMENT", "LESS_THAN", "LESS_THAN_OR_EQUAL", "GREATER_THAN", 
                  "GREATER_THAN_OR_EQUAL", "STRING_CONCATENATION", "STRING_COMPARISION", 
                  "NOT", "AND", "OR", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", 
                  "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", "COMMA", 
                  "NEWLINE", "NUMBER", "BOOLEAN", "STRING", "COMMENT", "IDENTIFIER", 
                  "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_TOKEN", 
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
            actions[42] = self.STRING_action 
            actions[46] = self.ILLEGAL_ESCAPE_action 
            actions[47] = self.UNCLOSE_STRING_action 
            actions[48] = self.ERROR_TOKEN_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise IllegalEscape(self.text[1:])
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise UncloseString(self.text[1:])
     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


