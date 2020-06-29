# babbaabbabaababaaabbbbbbbababbbabbbababaabbbbaaaaabbaababaaabaabbabababaabaabbbababaabbabbbababbaabb
# 860622337747
# 395886275361
import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    i = 0
    counta = 0
    for a in s:
        if a == 'a':
            counta += 1
    if counta == 0:
        return 0
    for str in s[:(n % len(s))]:
        if str == 'a':
            i += 1
    # print(i)
    occ = (int(n / len(s)) * counta) + i
    return occ


# print(repeatedString('babbaabbabaababaaabbbbbbbababbbabbbababaabbbbaaaaabbaababaaabaabbabababaabaabbbababaabbabbbababbaabb',860622337747))
print(repeatedString('d', 590826798023))
