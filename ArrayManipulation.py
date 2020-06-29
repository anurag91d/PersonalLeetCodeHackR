#!/bin/python3

import math
import os
import random
import re
import sys
from array import *


# import numpy

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    # k = 0
    max = 0
    arr = [0 for i in range(n)]
    for k in queries:
        m = k[0] - 1
        n = k[1] - 1
        o = k[2]
        for l in range(m,n+1):
            arr[l] += o
            if arr[l] > max:
                max = arr[l]
            # m += 1
        # k += 1
    return max


'''
BEST SOLUTION
    arr = [0]*n
    for i in queries:
        arr[i[0] - 1] += i[2]
        if i[1] != len(arr):
            arr[i[1]] -= i[2]
    maxval = 0
    itt = 0
    print(arr)
    for q in arr:
        itt += q
        if itt > maxval:
            maxval = itt
    return maxval'''

#
# 2 6 8
# 3 5 7
# 1 8 1
# 5 9 15
# queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
queries = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]
print(arrayManipulation(10, queries))
