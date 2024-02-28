# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *




def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01b7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3")
        buf.write("\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!")
        buf.write("\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3)\3)\3")
        buf.write(")\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3")
        buf.write("/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\62\3\62\3\62\3\62\3\62\7\62\u013e\n\62\f\62")
        buf.write("\16\62\u0141\13\62\3\62\5\62\u0144\n\62\3\63\3\63\3\63")
        buf.write("\5\63\u0149\n\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3")
        buf.write("\63\3\63\5\63\u0154\n\63\3\64\3\64\7\64\u0158\n\64\f\64")
        buf.write("\16\64\u015b\13\64\3\65\3\65\5\65\u015f\n\65\3\65\6\65")
        buf.write("\u0162\n\65\r\65\16\65\u0163\3\66\3\66\5\66\u0168\n\66")
        buf.write("\3\67\3\67\3\67\3\67\7\67\u016e\n\67\f\67\16\67\u0171")
        buf.write("\13\67\3\67\3\67\3\67\38\38\78\u0178\n8\f8\168\u017b\13")
        buf.write("8\39\39\39\39\79\u0181\n9\f9\169\u0184\139\39\39\39\3")
        buf.write("9\39\3:\3:\3:\3:\7:\u018f\n:\f:\16:\u0192\13:\3:\3:\3")
        buf.write(";\6;\u0197\n;\r;\16;\u0198\3;\3;\3<\3<\3<\3<\7<\u01a1")
        buf.write("\n<\f<\16<\u01a4\13<\3<\3<\3=\3=\3=\3=\7=\u01ac\n=\f=")
        buf.write("\16=\u01af\13=\3=\3=\3=\3=\3>\3>\3>\3\u0182\2?\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\2a\2c\61e\62g\2i\2k\63m\64o\65q\66s\67u8w9y")
        buf.write(":{;\3\2\f\3\2\63;\3\2\62;\4\2GGgg\4\2--//\6\2\f\f\17\17")
        buf.write("$$^^\n\2$$))^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\aac|\4\2")
        buf.write("\f\f\17\17\5\2\n\f\16\17\"\"\2\u01c6\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2c\3\2\2\2\2")
        buf.write("e\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2")
        buf.write("\2\3}\3\2\2\2\5\u0082\3\2\2\2\7\u0084\3\2\2\2\t\u0086")
        buf.write("\3\2\2\2\13\u0088\3\2\2\2\r\u008a\3\2\2\2\17\u008c\3\2")
        buf.write("\2\2\21\u008e\3\2\2\2\23\u0090\3\2\2\2\25\u0092\3\2\2")
        buf.write("\2\27\u0094\3\2\2\2\31\u0096\3\2\2\2\33\u0098\3\2\2\2")
        buf.write("\35\u009a\3\2\2\2\37\u009c\3\2\2\2!\u009e\3\2\2\2#\u00a0")
        buf.write("\3\2\2\2%\u00a2\3\2\2\2\'\u00a4\3\2\2\2)\u00a7\3\2\2\2")
        buf.write("+\u00aa\3\2\2\2-\u00ad\3\2\2\2/\u00b0\3\2\2\2\61\u00b2")
        buf.write("\3\2\2\2\63\u00b5\3\2\2\2\65\u00b7\3\2\2\2\67\u00ba\3")
        buf.write("\2\2\29\u00bd\3\2\2\2;\u00c2\3\2\2\2=\u00c8\3\2\2\2?\u00d0")
        buf.write("\3\2\2\2A\u00d3\3\2\2\2C\u00d8\3\2\2\2E\u00de\3\2\2\2")
        buf.write("G\u00e2\3\2\2\2I\u00eb\3\2\2\2K\u00ee\3\2\2\2M\u00f6\3")
        buf.write("\2\2\2O\u00fd\3\2\2\2Q\u0104\3\2\2\2S\u010a\3\2\2\2U\u010f")
        buf.write("\3\2\2\2W\u0113\3\2\2\2Y\u011c\3\2\2\2[\u011f\3\2\2\2")
        buf.write("]\u0127\3\2\2\2_\u012d\3\2\2\2a\u0132\3\2\2\2c\u0143\3")
        buf.write("\2\2\2e\u0153\3\2\2\2g\u0155\3\2\2\2i\u015c\3\2\2\2k\u0167")
        buf.write("\3\2\2\2m\u0169\3\2\2\2o\u0175\3\2\2\2q\u017c\3\2\2\2")
        buf.write("s\u018a\3\2\2\2u\u0196\3\2\2\2w\u019c\3\2\2\2y\u01a7\3")
        buf.write("\2\2\2{\u01b4\3\2\2\2}~\7g\2\2~\177\7n\2\2\177\u0080\7")
        buf.write("k\2\2\u0080\u0081\7h\2\2\u0081\4\3\2\2\2\u0082\u0083\7")
        buf.write("*\2\2\u0083\6\3\2\2\2\u0084\u0085\7+\2\2\u0085\b\3\2\2")
        buf.write("\2\u0086\u0087\7]\2\2\u0087\n\3\2\2\2\u0088\u0089\7_\2")
        buf.write("\2\u0089\f\3\2\2\2\u008a\u008b\7\60\2\2\u008b\16\3\2\2")
        buf.write("\2\u008c\u008d\7.\2\2\u008d\20\3\2\2\2\u008e\u008f\7=")
        buf.write("\2\2\u008f\22\3\2\2\2\u0090\u0091\7<\2\2\u0091\24\3\2")
        buf.write("\2\2\u0092\u0093\7}\2\2\u0093\26\3\2\2\2\u0094\u0095\7")
        buf.write("\177\2\2\u0095\30\3\2\2\2\u0096\u0097\7?\2\2\u0097\32")
        buf.write("\3\2\2\2\u0098\u0099\7-\2\2\u0099\34\3\2\2\2\u009a\u009b")
        buf.write("\7/\2\2\u009b\36\3\2\2\2\u009c\u009d\7,\2\2\u009d \3\2")
        buf.write("\2\2\u009e\u009f\7\61\2\2\u009f\"\3\2\2\2\u00a0\u00a1")
        buf.write("\7\'\2\2\u00a1$\3\2\2\2\u00a2\u00a3\7#\2\2\u00a3&\3\2")
        buf.write("\2\2\u00a4\u00a5\7(\2\2\u00a5\u00a6\7(\2\2\u00a6(\3\2")
        buf.write("\2\2\u00a7\u00a8\7~\2\2\u00a8\u00a9\7~\2\2\u00a9*\3\2")
        buf.write("\2\2\u00aa\u00ab\7?\2\2\u00ab\u00ac\7?\2\2\u00ac,\3\2")
        buf.write("\2\2\u00ad\u00ae\7#\2\2\u00ae\u00af\7?\2\2\u00af.\3\2")
        buf.write("\2\2\u00b0\u00b1\7>\2\2\u00b1\60\3\2\2\2\u00b2\u00b3\7")
        buf.write(">\2\2\u00b3\u00b4\7?\2\2\u00b4\62\3\2\2\2\u00b5\u00b6")
        buf.write("\7@\2\2\u00b6\64\3\2\2\2\u00b7\u00b8\7@\2\2\u00b8\u00b9")
        buf.write("\7?\2\2\u00b9\66\3\2\2\2\u00ba\u00bb\7<\2\2\u00bb\u00bc")
        buf.write("\7<\2\2\u00bc8\3\2\2\2\u00bd\u00be\7c\2\2\u00be\u00bf")
        buf.write("\7w\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1\7q\2\2\u00c1:\3")
        buf.write("\2\2\2\u00c2\u00c3\7d\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5")
        buf.write("\7g\2\2\u00c5\u00c6\7c\2\2\u00c6\u00c7\7m\2\2\u00c7<\3")
        buf.write("\2\2\2\u00c8\u00c9\7d\2\2\u00c9\u00ca\7q\2\2\u00ca\u00cb")
        buf.write("\7q\2\2\u00cb\u00cc\7n\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce")
        buf.write("\7c\2\2\u00ce\u00cf\7p\2\2\u00cf>\3\2\2\2\u00d0\u00d1")
        buf.write("\7f\2\2\u00d1\u00d2\7q\2\2\u00d2@\3\2\2\2\u00d3\u00d4")
        buf.write("\7g\2\2\u00d4\u00d5\7n\2\2\u00d5\u00d6\7u\2\2\u00d6\u00d7")
        buf.write("\7g\2\2\u00d7B\3\2\2\2\u00d8\u00d9\7h\2\2\u00d9\u00da")
        buf.write("\7n\2\2\u00da\u00db\7q\2\2\u00db\u00dc\7c\2\2\u00dc\u00dd")
        buf.write("\7v\2\2\u00ddD\3\2\2\2\u00de\u00df\7h\2\2\u00df\u00e0")
        buf.write("\7q\2\2\u00e0\u00e1\7t\2\2\u00e1F\3\2\2\2\u00e2\u00e3")
        buf.write("\7h\2\2\u00e3\u00e4\7w\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6")
        buf.write("\7e\2\2\u00e6\u00e7\7v\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9")
        buf.write("\7q\2\2\u00e9\u00ea\7p\2\2\u00eaH\3\2\2\2\u00eb\u00ec")
        buf.write("\7k\2\2\u00ec\u00ed\7h\2\2\u00edJ\3\2\2\2\u00ee\u00ef")
        buf.write("\7k\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f1\7v\2\2\u00f1\u00f2")
        buf.write("\7g\2\2\u00f2\u00f3\7i\2\2\u00f3\u00f4\7g\2\2\u00f4\u00f5")
        buf.write("\7t\2\2\u00f5L\3\2\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8")
        buf.write("\7g\2\2\u00f8\u00f9\7v\2\2\u00f9\u00fa\7w\2\2\u00fa\u00fb")
        buf.write("\7t\2\2\u00fb\u00fc\7p\2\2\u00fcN\3\2\2\2\u00fd\u00fe")
        buf.write("\7u\2\2\u00fe\u00ff\7v\2\2\u00ff\u0100\7t\2\2\u0100\u0101")
        buf.write("\7k\2\2\u0101\u0102\7p\2\2\u0102\u0103\7i\2\2\u0103P\3")
        buf.write("\2\2\2\u0104\u0105\7y\2\2\u0105\u0106\7j\2\2\u0106\u0107")
        buf.write("\7k\2\2\u0107\u0108\7n\2\2\u0108\u0109\7g\2\2\u0109R\3")
        buf.write("\2\2\2\u010a\u010b\7x\2\2\u010b\u010c\7q\2\2\u010c\u010d")
        buf.write("\7k\2\2\u010d\u010e\7f\2\2\u010eT\3\2\2\2\u010f\u0110")
        buf.write("\7q\2\2\u0110\u0111\7w\2\2\u0111\u0112\7v\2\2\u0112V\3")
        buf.write("\2\2\2\u0113\u0114\7e\2\2\u0114\u0115\7q\2\2\u0115\u0116")
        buf.write("\7p\2\2\u0116\u0117\7v\2\2\u0117\u0118\7k\2\2\u0118\u0119")
        buf.write("\7p\2\2\u0119\u011a\7w\2\2\u011a\u011b\7g\2\2\u011bX\3")
        buf.write("\2\2\2\u011c\u011d\7q\2\2\u011d\u011e\7h\2\2\u011eZ\3")
        buf.write("\2\2\2\u011f\u0120\7k\2\2\u0120\u0121\7p\2\2\u0121\u0122")
        buf.write("\7j\2\2\u0122\u0123\7g\2\2\u0123\u0124\7t\2\2\u0124\u0125")
        buf.write("\7k\2\2\u0125\u0126\7v\2\2\u0126\\\3\2\2\2\u0127\u0128")
        buf.write("\7c\2\2\u0128\u0129\7t\2\2\u0129\u012a\7t\2\2\u012a\u012b")
        buf.write("\7c\2\2\u012b\u012c\7{\2\2\u012c^\3\2\2\2\u012d\u012e")
        buf.write("\7v\2\2\u012e\u012f\7t\2\2\u012f\u0130\7w\2\2\u0130\u0131")
        buf.write("\7g\2\2\u0131`\3\2\2\2\u0132\u0133\7h\2\2\u0133\u0134")
        buf.write("\7c\2\2\u0134\u0135\7n\2\2\u0135\u0136\7u\2\2\u0136\u0137")
        buf.write("\7g\2\2\u0137b\3\2\2\2\u0138\u0144\7\62\2\2\u0139\u013f")
        buf.write("\t\2\2\2\u013a\u013b\7a\2\2\u013b\u013e\t\3\2\2\u013c")
        buf.write("\u013e\t\3\2\2\u013d\u013a\3\2\2\2\u013d\u013c\3\2\2\2")
        buf.write("\u013e\u0141\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140\3")
        buf.write("\2\2\2\u0140\u0142\3\2\2\2\u0141\u013f\3\2\2\2\u0142\u0144")
        buf.write("\b\62\2\2\u0143\u0138\3\2\2\2\u0143\u0139\3\2\2\2\u0144")
        buf.write("d\3\2\2\2\u0145\u0146\5c\62\2\u0146\u0148\5g\64\2\u0147")
        buf.write("\u0149\5i\65\2\u0148\u0147\3\2\2\2\u0148\u0149\3\2\2\2")
        buf.write("\u0149\u014a\3\2\2\2\u014a\u014b\b\63\3\2\u014b\u0154")
        buf.write("\3\2\2\2\u014c\u014d\5c\62\2\u014d\u014e\5i\65\2\u014e")
        buf.write("\u014f\b\63\4\2\u014f\u0154\3\2\2\2\u0150\u0151\5g\64")
        buf.write("\2\u0151\u0152\5i\65\2\u0152\u0154\3\2\2\2\u0153\u0145")
        buf.write("\3\2\2\2\u0153\u014c\3\2\2\2\u0153\u0150\3\2\2\2\u0154")
        buf.write("f\3\2\2\2\u0155\u0159\5\r\7\2\u0156\u0158\t\3\2\2\u0157")
        buf.write("\u0156\3\2\2\2\u0158\u015b\3\2\2\2\u0159\u0157\3\2\2\2")
        buf.write("\u0159\u015a\3\2\2\2\u015ah\3\2\2\2\u015b\u0159\3\2\2")
        buf.write("\2\u015c\u015e\t\4\2\2\u015d\u015f\t\5\2\2\u015e\u015d")
        buf.write("\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0161\3\2\2\2\u0160")
        buf.write("\u0162\t\3\2\2\u0161\u0160\3\2\2\2\u0162\u0163\3\2\2\2")
        buf.write("\u0163\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164j\3\2\2")
        buf.write("\2\u0165\u0168\5_\60\2\u0166\u0168\5a\61\2\u0167\u0165")
        buf.write("\3\2\2\2\u0167\u0166\3\2\2\2\u0168l\3\2\2\2\u0169\u016f")
        buf.write("\7$\2\2\u016a\u016e\n\6\2\2\u016b\u016c\7^\2\2\u016c\u016e")
        buf.write("\t\7\2\2\u016d\u016a\3\2\2\2\u016d\u016b\3\2\2\2\u016e")
        buf.write("\u0171\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u0170\3\2\2\2")
        buf.write("\u0170\u0172\3\2\2\2\u0171\u016f\3\2\2\2\u0172\u0173\7")
        buf.write("$\2\2\u0173\u0174\b\67\5\2\u0174n\3\2\2\2\u0175\u0179")
        buf.write("\t\b\2\2\u0176\u0178\t\t\2\2\u0177\u0176\3\2\2\2\u0178")
        buf.write("\u017b\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u017a\3\2\2\2")
        buf.write("\u017ap\3\2\2\2\u017b\u0179\3\2\2\2\u017c\u017d\7\61\2")
        buf.write("\2\u017d\u017e\7,\2\2\u017e\u0182\3\2\2\2\u017f\u0181")
        buf.write("\13\2\2\2\u0180\u017f\3\2\2\2\u0181\u0184\3\2\2\2\u0182")
        buf.write("\u0183\3\2\2\2\u0182\u0180\3\2\2\2\u0183\u0185\3\2\2\2")
        buf.write("\u0184\u0182\3\2\2\2\u0185\u0186\7,\2\2\u0186\u0187\7")
        buf.write("\61\2\2\u0187\u0188\3\2\2\2\u0188\u0189\b9\6\2\u0189r")
        buf.write("\3\2\2\2\u018a\u018b\7\61\2\2\u018b\u018c\7\61\2\2\u018c")
        buf.write("\u0190\3\2\2\2\u018d\u018f\n\n\2\2\u018e\u018d\3\2\2\2")
        buf.write("\u018f\u0192\3\2\2\2\u0190\u018e\3\2\2\2\u0190\u0191\3")
        buf.write("\2\2\2\u0191\u0193\3\2\2\2\u0192\u0190\3\2\2\2\u0193\u0194")
        buf.write("\b:\6\2\u0194t\3\2\2\2\u0195\u0197\t\13\2\2\u0196\u0195")
        buf.write("\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0196\3\2\2\2\u0198")
        buf.write("\u0199\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u019b\b;\6\2")
        buf.write("\u019bv\3\2\2\2\u019c\u01a2\7$\2\2\u019d\u01a1\n\6\2\2")
        buf.write("\u019e\u019f\7^\2\2\u019f\u01a1\t\7\2\2\u01a0\u019d\3")
        buf.write("\2\2\2\u01a0\u019e\3\2\2\2\u01a1\u01a4\3\2\2\2\u01a2\u01a0")
        buf.write("\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a5\3\2\2\2\u01a4")
        buf.write("\u01a2\3\2\2\2\u01a5\u01a6\b<\7\2\u01a6x\3\2\2\2\u01a7")
        buf.write("\u01ad\7$\2\2\u01a8\u01ac\n\6\2\2\u01a9\u01aa\7^\2\2\u01aa")
        buf.write("\u01ac\t\7\2\2\u01ab\u01a8\3\2\2\2\u01ab\u01a9\3\2\2\2")
        buf.write("\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3")
        buf.write("\2\2\2\u01ae\u01b0\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b1")
        buf.write("\7^\2\2\u01b1\u01b2\n\7\2\2\u01b2\u01b3\b=\b\2\u01b3z")
        buf.write("\3\2\2\2\u01b4\u01b5\13\2\2\2\u01b5\u01b6\b>\t\2\u01b6")
        buf.write("|\3\2\2\2\26\2\u013d\u013f\u0143\u0148\u0153\u0159\u015e")
        buf.write("\u0163\u0167\u016d\u016f\u0179\u0182\u0190\u0198\u01a0")
        buf.write("\u01a2\u01ab\u01ad\n\3\62\2\3\63\3\3\63\4\3\67\5\b\2\2")
        buf.write("\3<\6\3=\7\3>\b")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ELIF = 1
    LB = 2
    RB = 3
    LSP = 4
    RSP = 5
    DOT = 6
    CM = 7
    SEMI = 8
    CL = 9
    LCP = 10
    RCP = 11
    ASSIGN = 12
    ADDOP = 13
    SUBOP = 14
    MULOP = 15
    DIVOP = 16
    MODOP = 17
    NOT = 18
    AND = 19
    OR = 20
    EQUAL = 21
    NEQUAL = 22
    SMALL = 23
    SMALLEQ = 24
    LARGE = 25
    LARGEEQ = 26
    CONC = 27
    AUTO = 28
    BREAK = 29
    BOOLEAN = 30
    DO = 31
    ELSE = 32
    FLOAT = 33
    FOR = 34
    FUNCTION = 35
    IF = 36
    INTEGER = 37
    RETURN = 38
    STRING = 39
    WHILE = 40
    VOID = 41
    OUT = 42
    CONTINUE = 43
    OF = 44
    INHERIT = 45
    ARRAY = 46
    INTLIT = 47
    FLOATLIT = 48
    BOOLLIT = 49
    STRINGLIT = 50
    ID = 51
    CCOMMENT = 52
    CPPCOMMENT = 53
    WS = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56
    ERROR_CHAR = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'elif'", "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", 
            "'{'", "'}'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
            "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'::'", "'auto'", "'break'", "'boolean'", "'do'", "'else'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'while'", "'void'", "'out'", "'continue'", "'of'", 
            "'inherit'", "'array'" ]

    symbolicNames = [ "<INVALID>",
            "ELIF", "LB", "RB", "LSP", "RSP", "DOT", "CM", "SEMI", "CL", 
            "LCP", "RCP", "ASSIGN", "ADDOP", "SUBOP", "MULOP", "DIVOP", 
            "MODOP", "NOT", "AND", "OR", "EQUAL", "NEQUAL", "SMALL", "SMALLEQ", 
            "LARGE", "LARGEEQ", "CONC", "AUTO", "BREAK", "BOOLEAN", "DO", 
            "ELSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", 
            "STRING", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
            "ARRAY", "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", "ID", 
            "CCOMMENT", "CPPCOMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "ELIF", "LB", "RB", "LSP", "RSP", "DOT", "CM", "SEMI", 
                  "CL", "LCP", "RCP", "ASSIGN", "ADDOP", "SUBOP", "MULOP", 
                  "DIVOP", "MODOP", "NOT", "AND", "OR", "EQUAL", "NEQUAL", 
                  "SMALL", "SMALLEQ", "LARGE", "LARGEEQ", "CONC", "AUTO", 
                  "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", "FOR", "FUNCTION", 
                  "IF", "INTEGER", "RETURN", "STRING", "WHILE", "VOID", 
                  "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "TRUE", "FALSE", 
                  "INTLIT", "FLOATLIT", "DECPART", "EXPONENT", "BOOLLIT", 
                  "STRINGLIT", "ID", "CCOMMENT", "CPPCOMMENT", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[48] = self.INTLIT_action 
            actions[49] = self.FLOATLIT_action 
            actions[53] = self.STRINGLIT_action 
            actions[58] = self.UNCLOSE_STRING_action 
            actions[59] = self.ILLEGAL_ESCAPE_action 
            actions[60] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

        if actionIndex == 2:
            self.text = self.text.replace("_", "")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            raise ErrorToken(self.text)
     


