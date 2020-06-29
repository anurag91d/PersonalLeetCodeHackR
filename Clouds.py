#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i=0
    jumps = 0
    # print(len(c))
    # print(c[i+2])
    while i < len(c) - 1:
        if i+2 < len(c):
            if c[i+2] == 0:
                jumps += 1
                i+= 2
                # print(i)
            else:
                i+=1
                jumps += 1
        else:
            if i+1 == len(c):
                return jumps
            else:
                jumps +=1
                i += 1
                break
    return jumps


c = [0,0, 0, 0, 1, 0]
print(jumpingOnClouds(c))
