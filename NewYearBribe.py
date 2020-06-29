import math
import os
import random
import re
import sys
from array import *


# Complete the minimumBribes function below.
def minimumBribes(q):
    i = 0
    bribes = 0
    while i < len(q):
        diff = q[i] - (i + 1)
        if diff > 2:
            print("Too chaotic")
            return
        j=0
        while j < i:
            if q[j] > q[i]:
                bribes += 1
            j += 1
        i += 1
    return bribes


t1 = [2, 1, 5, 3, 4]
t2 = [2, 5, 1, 3, 4]
t3 = [5, 1, 2, 3, 7, 8, 6, 4]
t4 = [1, 2, 5, 3, 7, 8, 6, 4]
print(minimumBribes(t1))
print(minimumBribes(t2))
print(minimumBribes(t3))
print(minimumBribes(t4))
