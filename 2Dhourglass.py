import math
import os
import random
import re
import sys
from array import *


# Complete the hourglassSum function below.
def hourglassSum(arr):
    i = 0
    j = 0
    lim = len(arr)

    print(lim)
    max = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][
                    j + 1] + \
                       arr[i + 2][j + 2]
    while i < lim:
        j = 0
        while j < lim:
            # print(arr[i][j])
            if i + 2 < lim and j + 2 < lim:
                hsum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][
                    j + 1] + \
                       arr[i + 2][j + 2]
                # print(hsum)
                if hsum > max:
                    max = hsum
            j += 1
        i += 1
    return max


arr = [[-1, -1, 0, -9, -2, -2], [-2, -1, -6, -8, -2, -5], [-1, -1, -1, -2, -3, -4], [-1, -9, -2, -4, -4, -5],
       [-7, -3, -3, -2, -9, -9], [-1, -3, -1, -2, -4, -5]]

# arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0],
#        [0, 0, 1, 2, 4, 0]]
print(hourglassSum(arr))

'''
-1 -1 0 -9 -2 -2
-2 -1 -6 -8 -2 -5
-1 -1 -1 -2 -3 -4
-1 -9 -2 -4 -4 -5
-7 -3 -3 -2 -9 -9
-1 -3 -1 -2 -4 -5'''

'''
0 -4 -6 0 -7 -6
-1 -2 -6 -8 -3 -1
-8 -4 -2 -8 -8 -6
-3 -1 -2 -5 -7 -4
-3 -5 -3 -6 -6 -6
-3 -6 0 -8 -6 -7'''
