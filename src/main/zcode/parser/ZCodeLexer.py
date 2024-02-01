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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u0193\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!")
        buf.write("\3!\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\5+\u0115\n+\3+\3+\3,\3")
        buf.write(",\5,\u011b\n,\3,\5,\u011e\n,\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\5-\u0129\n-\3.\3.\3.\7.\u012e\n.\f.\16.\u0131\13.\3")
        buf.write(".\3.\3.\3/\3/\3/\3/\7/\u013a\n/\f/\16/\u013d\13/\3/\5")
        buf.write("/\u0140\n/\3/\3/\3/\3/\3\60\3\60\7\60\u0148\n\60\f\60")
        buf.write("\16\60\u014b\13\60\3\61\6\61\u014e\n\61\r\61\16\61\u014f")
        buf.write("\3\61\3\61\3\62\3\62\3\62\7\62\u0157\n\62\f\62\16\62\u015a")
        buf.write("\13\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\7\63\u0163\n")
        buf.write("\63\f\63\16\63\u0166\13\63\3\63\3\63\3\64\3\64\3\64\3")
        buf.write("\65\6\65\u016e\n\65\r\65\16\65\u016f\3\66\3\66\7\66\u0174")
        buf.write("\n\66\f\66\16\66\u0177\13\66\3\67\3\67\5\67\u017b\n\67")
        buf.write("\3\67\6\67\u017e\n\67\r\67\16\67\u017f\38\38\38\38\38")
        buf.write("\38\38\38\38\38\38\38\38\38\38\38\58\u0192\n8\3\u013b")
        buf.write("\29\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\2k\2m\2o\2\3")
        buf.write("\2\n\6\2\f\f\17\17$$^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\13")
        buf.write("\f\17\17\"\"\t\2))^^ddhhppttvv\3\2\62;\4\2GGgg\4\2--/")
        buf.write("/\2\u01a7\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\3q\3\2\2\2\5x\3\2\2\2\7}\3\2\2\2\t")
        buf.write("\u0084\3\2\2\2\13\u0089\3\2\2\2\r\u0090\3\2\2\2\17\u0094")
        buf.write("\3\2\2\2\21\u009c\3\2\2\2\23\u00a3\3\2\2\2\25\u00a8\3")
        buf.write("\2\2\2\27\u00ac\3\2\2\2\31\u00b2\3\2\2\2\33\u00b5\3\2")
        buf.write("\2\2\35\u00bb\3\2\2\2\37\u00c4\3\2\2\2!\u00c7\3\2\2\2")
        buf.write("#\u00cc\3\2\2\2%\u00d1\3\2\2\2\'\u00d7\3\2\2\2)\u00db")
        buf.write("\3\2\2\2+\u00dd\3\2\2\2-\u00df\3\2\2\2/\u00e1\3\2\2\2")
        buf.write("\61\u00e3\3\2\2\2\63\u00e5\3\2\2\2\65\u00e7\3\2\2\2\67")
        buf.write("\u00ea\3\2\2\29\u00ed\3\2\2\2;\u00ef\3\2\2\2=\u00f2\3")
        buf.write("\2\2\2?\u00f4\3\2\2\2A\u00f7\3\2\2\2C\u00fb\3\2\2\2E\u00fe")
        buf.write("\3\2\2\2G\u0102\3\2\2\2I\u0106\3\2\2\2K\u0109\3\2\2\2")
        buf.write("M\u010b\3\2\2\2O\u010d\3\2\2\2Q\u010f\3\2\2\2S\u0111\3")
        buf.write("\2\2\2U\u0114\3\2\2\2W\u0118\3\2\2\2Y\u0128\3\2\2\2[\u012a")
        buf.write("\3\2\2\2]\u0135\3\2\2\2_\u0145\3\2\2\2a\u014d\3\2\2\2")
        buf.write("c\u0153\3\2\2\2e\u015f\3\2\2\2g\u0169\3\2\2\2i\u016d\3")
        buf.write("\2\2\2k\u0171\3\2\2\2m\u0178\3\2\2\2o\u0191\3\2\2\2qr")
        buf.write("\7c\2\2rs\7u\2\2st\7u\2\2tu\7k\2\2uv\7i\2\2vw\7p\2\2w")
        buf.write("\4\3\2\2\2xy\7g\2\2yz\7z\2\2z{\7r\2\2{|\7t\2\2|\6\3\2")
        buf.write("\2\2}~\7p\2\2~\177\7w\2\2\177\u0080\7o\2\2\u0080\u0081")
        buf.write("\7d\2\2\u0081\u0082\7g\2\2\u0082\u0083\7t\2\2\u0083\b")
        buf.write("\3\2\2\2\u0084\u0085\7d\2\2\u0085\u0086\7q\2\2\u0086\u0087")
        buf.write("\7q\2\2\u0087\u0088\7n\2\2\u0088\n\3\2\2\2\u0089\u008a")
        buf.write("\7u\2\2\u008a\u008b\7v\2\2\u008b\u008c\7t\2\2\u008c\u008d")
        buf.write("\7k\2\2\u008d\u008e\7p\2\2\u008e\u008f\7i\2\2\u008f\f")
        buf.write("\3\2\2\2\u0090\u0091\7x\2\2\u0091\u0092\7c\2\2\u0092\u0093")
        buf.write("\7t\2\2\u0093\16\3\2\2\2\u0094\u0095\7f\2\2\u0095\u0096")
        buf.write("\7{\2\2\u0096\u0097\7p\2\2\u0097\u0098\7c\2\2\u0098\u0099")
        buf.write("\7o\2\2\u0099\u009a\7k\2\2\u009a\u009b\7e\2\2\u009b\20")
        buf.write("\3\2\2\2\u009c\u009d\7t\2\2\u009d\u009e\7g\2\2\u009e\u009f")
        buf.write("\7v\2\2\u009f\u00a0\7w\2\2\u00a0\u00a1\7t\2\2\u00a1\u00a2")
        buf.write("\7p\2\2\u00a2\22\3\2\2\2\u00a3\u00a4\7h\2\2\u00a4\u00a5")
        buf.write("\7w\2\2\u00a5\u00a6\7p\2\2\u00a6\u00a7\7e\2\2\u00a7\24")
        buf.write("\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9\u00aa\7q\2\2\u00aa\u00ab")
        buf.write("\7t\2\2\u00ab\26\3\2\2\2\u00ac\u00ad\7w\2\2\u00ad\u00ae")
        buf.write("\7p\2\2\u00ae\u00af\7v\2\2\u00af\u00b0\7k\2\2\u00b0\u00b1")
        buf.write("\7n\2\2\u00b1\30\3\2\2\2\u00b2\u00b3\7d\2\2\u00b3\u00b4")
        buf.write("\7{\2\2\u00b4\32\3\2\2\2\u00b5\u00b6\7d\2\2\u00b6\u00b7")
        buf.write("\7t\2\2\u00b7\u00b8\7g\2\2\u00b8\u00b9\7c\2\2\u00b9\u00ba")
        buf.write("\7m\2\2\u00ba\34\3\2\2\2\u00bb\u00bc\7e\2\2\u00bc\u00bd")
        buf.write("\7q\2\2\u00bd\u00be\7p\2\2\u00be\u00bf\7v\2\2\u00bf\u00c0")
        buf.write("\7k\2\2\u00c0\u00c1\7p\2\2\u00c1\u00c2\7w\2\2\u00c2\u00c3")
        buf.write("\7g\2\2\u00c3\36\3\2\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6")
        buf.write("\7h\2\2\u00c6 \3\2\2\2\u00c7\u00c8\7g\2\2\u00c8\u00c9")
        buf.write("\7n\2\2\u00c9\u00ca\7u\2\2\u00ca\u00cb\7g\2\2\u00cb\"")
        buf.write("\3\2\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce\7n\2\2\u00ce\u00cf")
        buf.write("\7k\2\2\u00cf\u00d0\7h\2\2\u00d0$\3\2\2\2\u00d1\u00d2")
        buf.write("\7d\2\2\u00d2\u00d3\7g\2\2\u00d3\u00d4\7i\2\2\u00d4\u00d5")
        buf.write("\7k\2\2\u00d5\u00d6\7p\2\2\u00d6&\3\2\2\2\u00d7\u00d8")
        buf.write("\7g\2\2\u00d8\u00d9\7p\2\2\u00d9\u00da\7f\2\2\u00da(\3")
        buf.write("\2\2\2\u00db\u00dc\7-\2\2\u00dc*\3\2\2\2\u00dd\u00de\7")
        buf.write("/\2\2\u00de,\3\2\2\2\u00df\u00e0\7,\2\2\u00e0.\3\2\2\2")
        buf.write("\u00e1\u00e2\7\61\2\2\u00e2\60\3\2\2\2\u00e3\u00e4\7\'")
        buf.write("\2\2\u00e4\62\3\2\2\2\u00e5\u00e6\7?\2\2\u00e6\64\3\2")
        buf.write("\2\2\u00e7\u00e8\7#\2\2\u00e8\u00e9\7?\2\2\u00e9\66\3")
        buf.write("\2\2\2\u00ea\u00eb\7>\2\2\u00eb\u00ec\7/\2\2\u00ec8\3")
        buf.write("\2\2\2\u00ed\u00ee\7>\2\2\u00ee:\3\2\2\2\u00ef\u00f0\7")
        buf.write(">\2\2\u00f0\u00f1\7?\2\2\u00f1<\3\2\2\2\u00f2\u00f3\7")
        buf.write("@\2\2\u00f3>\3\2\2\2\u00f4\u00f5\7@\2\2\u00f5\u00f6\7")
        buf.write("?\2\2\u00f6@\3\2\2\2\u00f7\u00f8\7\60\2\2\u00f8\u00f9")
        buf.write("\7\60\2\2\u00f9\u00fa\7\60\2\2\u00faB\3\2\2\2\u00fb\u00fc")
        buf.write("\7?\2\2\u00fc\u00fd\7?\2\2\u00fdD\3\2\2\2\u00fe\u00ff")
        buf.write("\7p\2\2\u00ff\u0100\7q\2\2\u0100\u0101\7v\2\2\u0101F\3")
        buf.write("\2\2\2\u0102\u0103\7c\2\2\u0103\u0104\7p\2\2\u0104\u0105")
        buf.write("\7f\2\2\u0105H\3\2\2\2\u0106\u0107\7q\2\2\u0107\u0108")
        buf.write("\7t\2\2\u0108J\3\2\2\2\u0109\u010a\7*\2\2\u010aL\3\2\2")
        buf.write("\2\u010b\u010c\7+\2\2\u010cN\3\2\2\2\u010d\u010e\7]\2")
        buf.write("\2\u010eP\3\2\2\2\u010f\u0110\7_\2\2\u0110R\3\2\2\2\u0111")
        buf.write("\u0112\7.\2\2\u0112T\3\2\2\2\u0113\u0115\7\17\2\2\u0114")
        buf.write("\u0113\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0116\3\2\2\2")
        buf.write("\u0116\u0117\7\f\2\2\u0117V\3\2\2\2\u0118\u011a\5i\65")
        buf.write("\2\u0119\u011b\5k\66\2\u011a\u0119\3\2\2\2\u011a\u011b")
        buf.write("\3\2\2\2\u011b\u011d\3\2\2\2\u011c\u011e\5m\67\2\u011d")
        buf.write("\u011c\3\2\2\2\u011d\u011e\3\2\2\2\u011eX\3\2\2\2\u011f")
        buf.write("\u0120\7v\2\2\u0120\u0121\7t\2\2\u0121\u0122\7w\2\2\u0122")
        buf.write("\u0129\7g\2\2\u0123\u0124\7h\2\2\u0124\u0125\7c\2\2\u0125")
        buf.write("\u0126\7n\2\2\u0126\u0127\7u\2\2\u0127\u0129\7g\2\2\u0128")
        buf.write("\u011f\3\2\2\2\u0128\u0123\3\2\2\2\u0129Z\3\2\2\2\u012a")
        buf.write("\u012f\7$\2\2\u012b\u012e\5o8\2\u012c\u012e\n\2\2\2\u012d")
        buf.write("\u012b\3\2\2\2\u012d\u012c\3\2\2\2\u012e\u0131\3\2\2\2")
        buf.write("\u012f\u012d\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u0132\3")
        buf.write("\2\2\2\u0131\u012f\3\2\2\2\u0132\u0133\7$\2\2\u0133\u0134")
        buf.write("\b.\2\2\u0134\\\3\2\2\2\u0135\u0136\7%\2\2\u0136\u0137")
        buf.write("\7%\2\2\u0137\u013b\3\2\2\2\u0138\u013a\13\2\2\2\u0139")
        buf.write("\u0138\3\2\2\2\u013a\u013d\3\2\2\2\u013b\u013c\3\2\2\2")
        buf.write("\u013b\u0139\3\2\2\2\u013c\u013f\3\2\2\2\u013d\u013b\3")
        buf.write("\2\2\2\u013e\u0140\7\17\2\2\u013f\u013e\3\2\2\2\u013f")
        buf.write("\u0140\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0142\7\f\2\2")
        buf.write("\u0142\u0143\3\2\2\2\u0143\u0144\b/\3\2\u0144^\3\2\2\2")
        buf.write("\u0145\u0149\t\3\2\2\u0146\u0148\t\4\2\2\u0147\u0146\3")
        buf.write("\2\2\2\u0148\u014b\3\2\2\2\u0149\u0147\3\2\2\2\u0149\u014a")
        buf.write("\3\2\2\2\u014a`\3\2\2\2\u014b\u0149\3\2\2\2\u014c\u014e")
        buf.write("\t\5\2\2\u014d\u014c\3\2\2\2\u014e\u014f\3\2\2\2\u014f")
        buf.write("\u014d\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0151\3\2\2\2")
        buf.write("\u0151\u0152\b\61\3\2\u0152b\3\2\2\2\u0153\u0158\7$\2")
        buf.write("\2\u0154\u0157\5o8\2\u0155\u0157\n\2\2\2\u0156\u0154\3")
        buf.write("\2\2\2\u0156\u0155\3\2\2\2\u0157\u015a\3\2\2\2\u0158\u0156")
        buf.write("\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015b\3\2\2\2\u015a")
        buf.write("\u0158\3\2\2\2\u015b\u015c\7^\2\2\u015c\u015d\n\6\2\2")
        buf.write("\u015d\u015e\b\62\4\2\u015ed\3\2\2\2\u015f\u0164\7$\2")
        buf.write("\2\u0160\u0163\5o8\2\u0161\u0163\n\2\2\2\u0162\u0160\3")
        buf.write("\2\2\2\u0162\u0161\3\2\2\2\u0163\u0166\3\2\2\2\u0164\u0162")
        buf.write("\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0167\3\2\2\2\u0166")
        buf.write("\u0164\3\2\2\2\u0167\u0168\b\63\5\2\u0168f\3\2\2\2\u0169")
        buf.write("\u016a\13\2\2\2\u016a\u016b\b\64\6\2\u016bh\3\2\2\2\u016c")
        buf.write("\u016e\t\7\2\2\u016d\u016c\3\2\2\2\u016e\u016f\3\2\2\2")
        buf.write("\u016f\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170j\3\2\2")
        buf.write("\2\u0171\u0175\13\2\2\2\u0172\u0174\t\7\2\2\u0173\u0172")
        buf.write("\3\2\2\2\u0174\u0177\3\2\2\2\u0175\u0173\3\2\2\2\u0175")
        buf.write("\u0176\3\2\2\2\u0176l\3\2\2\2\u0177\u0175\3\2\2\2\u0178")
        buf.write("\u017a\t\b\2\2\u0179\u017b\t\t\2\2\u017a\u0179\3\2\2\2")
        buf.write("\u017a\u017b\3\2\2\2\u017b\u017d\3\2\2\2\u017c\u017e\t")
        buf.write("\7\2\2\u017d\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u017d")
        buf.write("\3\2\2\2\u017f\u0180\3\2\2\2\u0180n\3\2\2\2\u0181\u0182")
        buf.write("\7^\2\2\u0182\u0192\7d\2\2\u0183\u0184\7^\2\2\u0184\u0192")
        buf.write("\7h\2\2\u0185\u0186\7^\2\2\u0186\u0192\7t\2\2\u0187\u0188")
        buf.write("\7^\2\2\u0188\u0192\7p\2\2\u0189\u018a\7^\2\2\u018a\u0192")
        buf.write("\7v\2\2\u018b\u018c\7^\2\2\u018c\u0192\7)\2\2\u018d\u018e")
        buf.write("\7^\2\2\u018e\u0192\7^\2\2\u018f\u0190\7)\2\2\u0190\u0192")
        buf.write("\7$\2\2\u0191\u0181\3\2\2\2\u0191\u0183\3\2\2\2\u0191")
        buf.write("\u0185\3\2\2\2\u0191\u0187\3\2\2\2\u0191\u0189\3\2\2\2")
        buf.write("\u0191\u018b\3\2\2\2\u0191\u018d\3\2\2\2\u0191\u018f\3")
        buf.write("\2\2\2\u0192p\3\2\2\2\26\2\u0114\u011a\u011d\u0128\u012d")
        buf.write("\u012f\u013b\u013f\u0149\u014f\u0156\u0158\u0162\u0164")
        buf.write("\u016f\u0175\u017a\u017f\u0191\7\3.\2\b\2\2\3\62\3\3\63")
        buf.write("\4\3\64\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    TYPE_NUMBER = 3
    TYPE_BOOL = 4
    TYPE_STRING = 5
    VAR = 6
    DYNAMIC = 7
    RETURN = 8
    FUNCTION = 9
    FOR = 10
    UNTIL = 11
    BY = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSE = 16
    ELIF = 17
    BEGIN = 18
    END = 19
    PLUS = 20
    MINUS = 21
    MULTIPLY = 22
    DIVIDE = 23
    MODULO = 24
    EQUAL = 25
    NOT_EQUAL = 26
    ASSIGNMENT = 27
    LESS_THAN = 28
    LESS_THAN_OR_EQUAL = 29
    GREATER_THAN = 30
    GREATER_THAN_OR_EQUAL = 31
    STRING_CONCATENATION = 32
    STRING_COMPARISION = 33
    NOT = 34
    AND = 35
    OR = 36
    LEFT_PARENTHESIS = 37
    RIGHT_PARENTHESIS = 38
    LEFT_SQUARE_BRACKET = 39
    RIGHT_SQUARE_BRACKET = 40
    COMMA = 41
    NEWLINE = 42
    NUMBER = 43
    BOOLEAN = 44
    STRING = 45
    COMMENT = 46
    IDENTIFIER = 47
    WS = 48
    ILLEGAL_ESCAPE = 49
    UNCLOSE_STRING = 50
    ERROR_CHAR = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'assign'", "'expr'", "'number'", "'bool'", "'string'", "'var'", 
            "'dynamic'", "'return'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'!='", "'<-'", 
            "'<'", "'<='", "'>'", "'>='", "'...'", "'=='", "'not'", "'and'", 
            "'or'", "'('", "')'", "'['", "']'", "','" ]

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
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "TYPE_NUMBER", "TYPE_BOOL", "TYPE_STRING", 
                  "VAR", "DYNAMIC", "RETURN", "FUNCTION", "FOR", "UNTIL", 
                  "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                  "END", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MODULO", 
                  "EQUAL", "NOT_EQUAL", "ASSIGNMENT", "LESS_THAN", "LESS_THAN_OR_EQUAL", 
                  "GREATER_THAN", "GREATER_THAN_OR_EQUAL", "STRING_CONCATENATION", 
                  "STRING_COMPARISION", "NOT", "AND", "OR", "LEFT_PARENTHESIS", 
                  "RIGHT_PARENTHESIS", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
                  "COMMA", "NEWLINE", "NUMBER", "BOOLEAN", "STRING", "COMMENT", 
                  "IDENTIFIER", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "ERROR_CHAR", "INTEGER", "DECIMAL", "EXPONENT", "ESCAPE_SEQUENCE" ]

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
            actions[44] = self.STRING_action 
            actions[48] = self.ILLEGAL_ESCAPE_action 
            actions[49] = self.UNCLOSE_STRING_action 
            actions[50] = self.ERROR_CHAR_action 
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
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


