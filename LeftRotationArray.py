#!/bin/python3

import math
import os
import random
import re
import sys
from array import *
# Complete the rotLeft function below.
def rotLeft(a, d):
    return a[d:] + a[:d]
    # i=1
    # length = len(a)
    # while i <= d:
    #     temp = a[0]
    #     # print(temp)
    #     k=0
    #     while k < length and k+1 < length:
    #         # print(a[k],a[k+1])
    #         a[k] = a[k+1]
    #         # print(a[k],a[k+1])
    #         k +=1
    #     a[k] = temp
    #     # print(a[k])
    #     i +=1
    # # print("here")
    #
    # return a
    
    
arr = [1, 2, 3, 4, 5, 6]
print(rotLeft(arr,6))
