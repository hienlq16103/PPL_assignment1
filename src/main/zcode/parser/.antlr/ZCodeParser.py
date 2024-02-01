# Generated from e:/PPL/assignment1/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,49,488,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,1,0,
        1,0,1,0,1,1,1,1,1,1,1,1,3,1,126,8,1,1,2,1,2,3,2,130,8,2,1,3,1,3,
        3,3,134,8,3,1,3,1,3,1,3,1,3,3,3,140,8,3,1,3,1,3,1,3,1,3,1,3,1,3,
        3,3,148,8,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,160,8,6,
        1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,172,8,8,1,9,1,9,1,9,
        1,9,1,9,3,9,179,8,9,1,10,1,10,1,10,1,10,1,10,3,10,186,8,10,1,11,
        1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,3,12,197,8,12,1,13,1,13,
        1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,3,15,
        213,8,15,1,16,1,16,1,16,1,16,1,16,3,16,220,8,16,1,17,1,17,1,17,1,
        17,3,17,226,8,17,1,18,1,18,3,18,230,8,18,1,18,3,18,233,8,18,1,19,
        1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,3,20,245,8,20,1,21,
        1,21,3,21,249,8,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,
        259,8,22,1,23,1,23,3,23,263,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,
        24,3,24,272,8,24,1,25,1,25,1,25,1,25,1,25,3,25,279,8,25,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,3,26,288,8,26,1,27,1,27,1,27,1,27,1,27,
        1,27,1,27,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,30,1,30,1,30,
        1,30,3,30,309,8,30,1,31,1,31,1,31,1,31,3,31,315,8,31,1,32,1,32,1,
        32,1,32,1,32,1,32,1,32,3,32,324,8,32,1,33,1,33,1,33,1,33,1,33,1,
        33,1,33,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,35,1,35,3,
        35,344,8,35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,1,37,1,37,1,
        37,1,38,1,38,1,38,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,41,1,
        41,1,41,1,41,3,41,372,8,41,1,42,1,42,1,42,1,42,1,42,3,42,379,8,42,
        1,43,1,43,1,43,1,43,1,43,3,43,386,8,43,1,44,1,44,1,44,1,44,1,44,
        3,44,393,8,44,1,45,1,45,1,45,1,45,1,45,1,45,5,45,401,8,45,10,45,
        12,45,404,9,45,1,46,1,46,1,46,1,46,1,46,1,46,5,46,412,8,46,10,46,
        12,46,415,9,46,1,47,1,47,1,47,1,47,1,47,1,47,5,47,423,8,47,10,47,
        12,47,426,9,47,1,48,1,48,1,48,3,48,431,8,48,1,49,1,49,1,49,3,49,
        436,8,49,1,50,1,50,1,50,1,50,1,50,1,50,1,50,3,50,445,8,50,1,51,1,
        51,1,51,1,51,1,52,1,52,1,53,1,53,3,53,455,8,53,1,53,1,53,1,53,1,
        53,1,54,1,54,1,54,1,54,1,54,1,55,1,55,1,55,1,55,1,55,1,56,1,56,1,
        56,1,56,1,56,3,56,476,8,56,1,57,1,57,1,57,3,57,481,8,57,1,58,1,58,
        1,58,3,58,486,8,58,1,58,0,3,90,92,94,59,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,
        64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,
        106,108,110,112,114,116,0,6,1,0,1,3,1,0,4,5,1,0,33,34,1,0,18,19,
        1,0,20,22,3,0,23,24,26,29,31,31,480,0,118,1,0,0,0,2,125,1,0,0,0,
        4,129,1,0,0,0,6,147,1,0,0,0,8,149,1,0,0,0,10,151,1,0,0,0,12,153,
        1,0,0,0,14,163,1,0,0,0,16,171,1,0,0,0,18,178,1,0,0,0,20,185,1,0,
        0,0,22,187,1,0,0,0,24,196,1,0,0,0,26,198,1,0,0,0,28,204,1,0,0,0,
        30,212,1,0,0,0,32,219,1,0,0,0,34,221,1,0,0,0,36,232,1,0,0,0,38,234,
        1,0,0,0,40,244,1,0,0,0,42,248,1,0,0,0,44,258,1,0,0,0,46,262,1,0,
        0,0,48,271,1,0,0,0,50,278,1,0,0,0,52,280,1,0,0,0,54,289,1,0,0,0,
        56,296,1,0,0,0,58,300,1,0,0,0,60,308,1,0,0,0,62,314,1,0,0,0,64,316,
        1,0,0,0,66,325,1,0,0,0,68,332,1,0,0,0,70,343,1,0,0,0,72,349,1,0,
        0,0,74,353,1,0,0,0,76,356,1,0,0,0,78,359,1,0,0,0,80,362,1,0,0,0,
        82,371,1,0,0,0,84,378,1,0,0,0,86,385,1,0,0,0,88,392,1,0,0,0,90,394,
        1,0,0,0,92,405,1,0,0,0,94,416,1,0,0,0,96,430,1,0,0,0,98,435,1,0,
        0,0,100,444,1,0,0,0,102,446,1,0,0,0,104,450,1,0,0,0,106,454,1,0,
        0,0,108,460,1,0,0,0,110,465,1,0,0,0,112,475,1,0,0,0,114,480,1,0,
        0,0,116,485,1,0,0,0,118,119,3,2,1,0,119,120,5,0,0,1,120,1,1,0,0,
        0,121,122,3,4,2,0,122,123,3,2,1,0,123,126,1,0,0,0,124,126,3,4,2,
        0,125,121,1,0,0,0,125,124,1,0,0,0,126,3,1,0,0,0,127,130,3,6,3,0,
        128,130,3,26,13,0,129,127,1,0,0,0,129,128,1,0,0,0,130,5,1,0,0,0,
        131,134,3,8,4,0,132,134,5,5,0,0,133,131,1,0,0,0,133,132,1,0,0,0,
        134,135,1,0,0,0,135,136,5,45,0,0,136,148,3,114,57,0,137,140,3,8,
        4,0,138,140,3,10,5,0,139,137,1,0,0,0,139,138,1,0,0,0,140,141,1,0,
        0,0,141,142,5,45,0,0,142,143,5,25,0,0,143,144,3,86,43,0,144,145,
        3,114,57,0,145,148,1,0,0,0,146,148,3,12,6,0,147,133,1,0,0,0,147,
        139,1,0,0,0,147,146,1,0,0,0,148,7,1,0,0,0,149,150,7,0,0,0,150,9,
        1,0,0,0,151,152,7,1,0,0,152,11,1,0,0,0,153,154,3,8,4,0,154,155,5,
        45,0,0,155,159,3,14,7,0,156,157,5,25,0,0,157,160,3,18,9,0,158,160,
        1,0,0,0,159,156,1,0,0,0,159,158,1,0,0,0,160,161,1,0,0,0,161,162,
        3,114,57,0,162,13,1,0,0,0,163,164,5,37,0,0,164,165,3,16,8,0,165,
        166,5,38,0,0,166,15,1,0,0,0,167,168,5,41,0,0,168,169,5,39,0,0,169,
        172,3,16,8,0,170,172,5,41,0,0,171,167,1,0,0,0,171,170,1,0,0,0,172,
        17,1,0,0,0,173,179,3,22,11,0,174,175,5,37,0,0,175,176,3,20,10,0,
        176,177,5,38,0,0,177,179,1,0,0,0,178,173,1,0,0,0,178,174,1,0,0,0,
        179,19,1,0,0,0,180,181,3,22,11,0,181,182,5,39,0,0,182,183,3,20,10,
        0,183,186,1,0,0,0,184,186,3,22,11,0,185,180,1,0,0,0,185,184,1,0,
        0,0,186,21,1,0,0,0,187,188,5,37,0,0,188,189,3,24,12,0,189,190,5,
        38,0,0,190,23,1,0,0,0,191,192,3,86,43,0,192,193,5,39,0,0,193,194,
        3,24,12,0,194,197,1,0,0,0,195,197,3,86,43,0,196,191,1,0,0,0,196,
        195,1,0,0,0,197,25,1,0,0,0,198,199,5,7,0,0,199,200,5,45,0,0,200,
        201,3,28,14,0,201,202,3,116,58,0,202,203,3,36,18,0,203,27,1,0,0,
        0,204,205,5,35,0,0,205,206,3,30,15,0,206,207,5,36,0,0,207,29,1,0,
        0,0,208,209,3,34,17,0,209,210,3,32,16,0,210,213,1,0,0,0,211,213,
        1,0,0,0,212,208,1,0,0,0,212,211,1,0,0,0,213,31,1,0,0,0,214,215,5,
        39,0,0,215,216,3,34,17,0,216,217,3,32,16,0,217,220,1,0,0,0,218,220,
        1,0,0,0,219,214,1,0,0,0,219,218,1,0,0,0,220,33,1,0,0,0,221,222,3,
        8,4,0,222,225,5,45,0,0,223,226,3,14,7,0,224,226,1,0,0,0,225,223,
        1,0,0,0,225,224,1,0,0,0,226,35,1,0,0,0,227,230,3,38,19,0,228,230,
        3,72,36,0,229,227,1,0,0,0,229,228,1,0,0,0,230,233,1,0,0,0,231,233,
        3,114,57,0,232,229,1,0,0,0,232,231,1,0,0,0,233,37,1,0,0,0,234,235,
        5,16,0,0,235,236,3,114,57,0,236,237,3,40,20,0,237,238,5,17,0,0,238,
        239,3,114,57,0,239,39,1,0,0,0,240,241,3,42,21,0,241,242,3,40,20,
        0,242,245,1,0,0,0,243,245,1,0,0,0,244,240,1,0,0,0,244,243,1,0,0,
        0,245,41,1,0,0,0,246,249,3,44,22,0,247,249,3,46,23,0,248,246,1,0,
        0,0,248,247,1,0,0,0,249,43,1,0,0,0,250,259,3,6,3,0,251,259,3,70,
        35,0,252,259,3,74,37,0,253,259,3,76,38,0,254,259,3,72,36,0,255,259,
        3,78,39,0,256,259,3,38,19,0,257,259,3,68,34,0,258,250,1,0,0,0,258,
        251,1,0,0,0,258,252,1,0,0,0,258,253,1,0,0,0,258,254,1,0,0,0,258,
        255,1,0,0,0,258,256,1,0,0,0,258,257,1,0,0,0,259,45,1,0,0,0,260,263,
        3,48,24,0,261,263,3,50,25,0,262,260,1,0,0,0,262,261,1,0,0,0,263,
        47,1,0,0,0,264,265,3,52,26,0,265,266,3,60,30,0,266,272,1,0,0,0,267,
        268,3,54,27,0,268,269,3,62,31,0,269,270,3,56,28,0,270,272,1,0,0,
        0,271,264,1,0,0,0,271,267,1,0,0,0,272,49,1,0,0,0,273,279,3,44,22,
        0,274,275,3,54,27,0,275,276,3,62,31,0,276,277,3,58,29,0,277,279,
        1,0,0,0,278,273,1,0,0,0,278,274,1,0,0,0,279,51,1,0,0,0,280,281,5,
        13,0,0,281,282,5,35,0,0,282,283,3,86,43,0,283,284,5,36,0,0,284,287,
        3,116,58,0,285,288,3,44,22,0,286,288,3,48,24,0,287,285,1,0,0,0,287,
        286,1,0,0,0,288,53,1,0,0,0,289,290,5,13,0,0,290,291,5,35,0,0,291,
        292,3,86,43,0,292,293,5,36,0,0,293,294,3,116,58,0,294,295,3,50,25,
        0,295,55,1,0,0,0,296,297,5,14,0,0,297,298,3,116,58,0,298,299,3,48,
        24,0,299,57,1,0,0,0,300,301,5,14,0,0,301,302,3,116,58,0,302,303,
        3,50,25,0,303,59,1,0,0,0,304,305,3,64,32,0,305,306,3,60,30,0,306,
        309,1,0,0,0,307,309,1,0,0,0,308,304,1,0,0,0,308,307,1,0,0,0,309,
        61,1,0,0,0,310,311,3,66,33,0,311,312,3,62,31,0,312,315,1,0,0,0,313,
        315,1,0,0,0,314,310,1,0,0,0,314,313,1,0,0,0,315,63,1,0,0,0,316,317,
        5,15,0,0,317,318,5,35,0,0,318,319,3,86,43,0,319,320,5,36,0,0,320,
        323,3,116,58,0,321,324,3,44,22,0,322,324,3,48,24,0,323,321,1,0,0,
        0,323,322,1,0,0,0,324,65,1,0,0,0,325,326,5,15,0,0,326,327,5,35,0,
        0,327,328,3,86,43,0,328,329,5,36,0,0,329,330,3,116,58,0,330,331,
        3,50,25,0,331,67,1,0,0,0,332,333,5,8,0,0,333,334,5,45,0,0,334,335,
        5,9,0,0,335,336,3,86,43,0,336,337,5,10,0,0,337,338,3,86,43,0,338,
        339,3,116,58,0,339,340,3,42,21,0,340,69,1,0,0,0,341,344,5,45,0,0,
        342,344,3,110,55,0,343,341,1,0,0,0,343,342,1,0,0,0,344,345,1,0,0,
        0,345,346,5,25,0,0,346,347,3,86,43,0,347,348,3,114,57,0,348,71,1,
        0,0,0,349,350,5,6,0,0,350,351,3,86,43,0,351,352,3,114,57,0,352,73,
        1,0,0,0,353,354,5,11,0,0,354,355,3,114,57,0,355,75,1,0,0,0,356,357,
        5,12,0,0,357,358,3,114,57,0,358,77,1,0,0,0,359,360,3,80,40,0,360,
        361,3,114,57,0,361,79,1,0,0,0,362,363,5,45,0,0,363,364,5,35,0,0,
        364,365,3,82,41,0,365,366,5,36,0,0,366,81,1,0,0,0,367,368,3,86,43,
        0,368,369,3,84,42,0,369,372,1,0,0,0,370,372,1,0,0,0,371,367,1,0,
        0,0,371,370,1,0,0,0,372,83,1,0,0,0,373,374,5,39,0,0,374,375,3,86,
        43,0,375,376,3,84,42,0,376,379,1,0,0,0,377,379,1,0,0,0,378,373,1,
        0,0,0,378,377,1,0,0,0,379,85,1,0,0,0,380,381,3,88,44,0,381,382,5,
        30,0,0,382,383,3,88,44,0,383,386,1,0,0,0,384,386,3,88,44,0,385,380,
        1,0,0,0,385,384,1,0,0,0,386,87,1,0,0,0,387,388,3,90,45,0,388,389,
        3,104,52,0,389,390,3,90,45,0,390,393,1,0,0,0,391,393,3,90,45,0,392,
        387,1,0,0,0,392,391,1,0,0,0,393,89,1,0,0,0,394,395,6,45,-1,0,395,
        396,3,92,46,0,396,402,1,0,0,0,397,398,10,2,0,0,398,399,7,2,0,0,399,
        401,3,92,46,0,400,397,1,0,0,0,401,404,1,0,0,0,402,400,1,0,0,0,402,
        403,1,0,0,0,403,91,1,0,0,0,404,402,1,0,0,0,405,406,6,46,-1,0,406,
        407,3,94,47,0,407,413,1,0,0,0,408,409,10,2,0,0,409,410,7,3,0,0,410,
        412,3,94,47,0,411,408,1,0,0,0,412,415,1,0,0,0,413,411,1,0,0,0,413,
        414,1,0,0,0,414,93,1,0,0,0,415,413,1,0,0,0,416,417,6,47,-1,0,417,
        418,3,96,48,0,418,424,1,0,0,0,419,420,10,2,0,0,420,421,7,4,0,0,421,
        423,3,96,48,0,422,419,1,0,0,0,423,426,1,0,0,0,424,422,1,0,0,0,424,
        425,1,0,0,0,425,95,1,0,0,0,426,424,1,0,0,0,427,428,5,32,0,0,428,
        431,3,96,48,0,429,431,3,98,49,0,430,427,1,0,0,0,430,429,1,0,0,0,
        431,97,1,0,0,0,432,433,5,19,0,0,433,436,3,98,49,0,434,436,3,100,
        50,0,435,432,1,0,0,0,435,434,1,0,0,0,436,99,1,0,0,0,437,445,5,41,
        0,0,438,445,5,42,0,0,439,445,5,43,0,0,440,445,5,45,0,0,441,445,3,
        106,53,0,442,445,3,80,40,0,443,445,3,102,51,0,444,437,1,0,0,0,444,
        438,1,0,0,0,444,439,1,0,0,0,444,440,1,0,0,0,444,441,1,0,0,0,444,
        442,1,0,0,0,444,443,1,0,0,0,445,101,1,0,0,0,446,447,5,35,0,0,447,
        448,3,86,43,0,448,449,5,36,0,0,449,103,1,0,0,0,450,451,7,5,0,0,451,
        105,1,0,0,0,452,455,5,45,0,0,453,455,3,80,40,0,454,452,1,0,0,0,454,
        453,1,0,0,0,455,456,1,0,0,0,456,457,5,37,0,0,457,458,3,112,56,0,
        458,459,5,38,0,0,459,107,1,0,0,0,460,461,3,80,40,0,461,462,5,37,
        0,0,462,463,3,112,56,0,463,464,5,38,0,0,464,109,1,0,0,0,465,466,
        5,45,0,0,466,467,5,37,0,0,467,468,3,112,56,0,468,469,5,38,0,0,469,
        111,1,0,0,0,470,471,3,86,43,0,471,472,5,39,0,0,472,473,3,112,56,
        0,473,476,1,0,0,0,474,476,3,86,43,0,475,470,1,0,0,0,475,474,1,0,
        0,0,476,113,1,0,0,0,477,478,5,40,0,0,478,481,3,114,57,0,479,481,
        5,40,0,0,480,477,1,0,0,0,480,479,1,0,0,0,481,115,1,0,0,0,482,483,
        5,40,0,0,483,486,3,114,57,0,484,486,1,0,0,0,485,482,1,0,0,0,485,
        484,1,0,0,0,486,117,1,0,0,0,40,125,129,133,139,147,159,171,178,185,
        196,212,219,225,229,232,244,248,258,262,271,278,287,308,314,323,
        343,371,378,385,392,402,413,424,430,435,444,454,475,480,485
    ]

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
        self.checkVersion("4.13.1")
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




    def declaration(self):

        localctx = ZCodeParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.variable_declaration()
                pass
            elif token in [7]:
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
                if token in [1, 2, 3]:
                    self.state = 131
                    self.primitive_type()
                    pass
                elif token in [5]:
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
                if token in [1, 2, 3]:
                    self.state = 137
                    self.primitive_type()
                    pass
                elif token in [4, 5]:
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




    def primitive_type(self):

        localctx = ZCodeParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
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




    def impicit_type(self):

        localctx = ZCodeParser.Impicit_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_impicit_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
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
            if token in [25]:
                self.state = 156
                self.match(ZCodeParser.ASSIGNMENT)
                self.state = 157
                self.array_value()
                pass
            elif token in [40]:
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




    def parameter_list(self):

        localctx = ZCodeParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_parameter_list)
        try:
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.parameter()
                self.state = 209
                self.extra_parameter()
                pass
            elif token in [36]:
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




    def extra_parameter(self):

        localctx = ZCodeParser.Extra_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_extra_parameter)
        try:
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(ZCodeParser.COMMA)
                self.state = 215
                self.parameter()
                self.state = 216
                self.extra_parameter()
                pass
            elif token in [36]:
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
            if token in [37]:
                self.state = 223
                self.array_size()
                pass
            elif token in [36, 39]:
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




    def function_body(self):

        localctx = ZCodeParser.Function_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_function_body)
        try:
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [16]:
                    self.state = 227
                    self.block()
                    pass
                elif token in [6]:
                    self.state = 228
                    self.return_statement()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [40]:
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




    def statement_list(self):

        localctx = ZCodeParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_statement_list)
        try:
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 8, 11, 12, 13, 16, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.statement()
                self.state = 241
                self.statement_list()
                pass
            elif token in [17]:
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




    def close_statement(self):

        localctx = ZCodeParser.Close_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_close_statement)
        try:
            self.state = 278
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 8, 11, 12, 16, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.simple_statement()
                pass
            elif token in [13]:
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
            if token in [1, 2, 3, 4, 5, 6, 8, 11, 12, 16, 45]:
                self.state = 285
                self.simple_statement()
                pass
            elif token in [13]:
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




    def close_elif_list(self):

        localctx = ZCodeParser.Close_elif_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_close_elif_list)
        try:
            self.state = 314
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.close_elif()
                self.state = 311
                self.close_elif_list()
                pass
            elif token in [14]:
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
            if token in [1, 2, 3, 4, 5, 6, 8, 11, 12, 16, 45]:
                self.state = 321
                self.simple_statement()
                pass
            elif token in [13]:
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




    def argument_list(self):

        localctx = ZCodeParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_argument_list)
        try:
            self.state = 371
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 32, 35, 41, 42, 43, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.expression()
                self.state = 368
                self.extra_argument_list()
                pass
            elif token in [36]:
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




    def extra_argument_list(self):

        localctx = ZCodeParser.Extra_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_extra_argument_list)
        try:
            self.state = 378
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.match(ZCodeParser.COMMA)
                self.state = 374
                self.expression()
                self.state = 375
                self.extra_argument_list()
                pass
            elif token in [36]:
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
                    if not(_la==33 or _la==34):
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
                    if not(_la==18 or _la==19):
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
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0)):
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




    def expression5(self):

        localctx = ZCodeParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_expression5)
        try:
            self.state = 430
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.match(ZCodeParser.NOT)
                self.state = 428
                self.expression5()
                pass
            elif token in [19, 35, 41, 42, 43, 45]:
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




    def expression6(self):

        localctx = ZCodeParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_expression6)
        try:
            self.state = 435
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                self.match(ZCodeParser.MINUS)
                self.state = 433
                self.expression6()
                pass
            elif token in [35, 41, 42, 43, 45]:
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




    def relational_operator(self):

        localctx = ZCodeParser.Relational_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_relational_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3179282432) != 0)):
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

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nullable_newline_list




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
                self.newline_list()
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
         




