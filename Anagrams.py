#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def calc(check1, check2):
    # map1 = [0]*26
    # print(map1)
    # # map2 = {}
    # count =0
    # i=0
    # j=0
    # for i in range(len(check1)):
    #     map1[ord(check1[i])-ord('a')] += 1
    # print(map1)
    # for j in range(len(check2)):
    #     map1[ord(check2[j])-ord('a')] -= 1
    #     if map1[ord(check2[j])-ord('a')] < 0:
    #         count += 1
    # print(map1)
    map1 = {}
    map2 = {}
    for i in check1:
        map1[i] = map1.get(i, 0) + 1
    for j in check2:
        map2[j] = map2.get(j, 0) + 1
    count = 0
    # print(map1, map2)
    for k in map2:
        if k not in map1.keys():
            count += map2[k]
        else:
            if map1[k] < map2[k]:
                count += map2[k] - map1[k]
    return count


def anagram(s):
    if len(s) % 2 != 0:
        return -1
    else:
        s1 = s[0:int(len(s) / 2)]
        s2 = s[int(len(s) / 2):]
        result = calc(s1, s2)
        if result == 0:
            return 0
        else:
            return result


# print(anagram("aaabbb"))
# print(anagram("ab"))
# print(anagram("abc"))
# print(anagram("mnop"))
# print(anagram("xyyx"))
# print(anagram("xaxbbbxx"))
# print(anagram("abcdabcc"))
print(anagram("fdhlvosfpafhalll"))
