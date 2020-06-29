#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    # print (magazine)
    # print(note)
    mag = {}
    NOTE = {}
    for key in magazine:
        mag[key] = mag.get(key, 0) + 1
    for word in note:
        NOTE[word] = NOTE.get(word, 0) + 1
    # print(len(NOTE))
    # print(mag,NOTE)
    for i in NOTE:
        # print(i)
        if i not in mag.keys() or mag[i] < NOTE[i]:
            print("No")
            return
    print("Yes")
    return

magazine = ['h' , 'ghq' , 'g' , 'xxy' , 'wdnr' , 'anjst', 'xxy', 'wdnr', 'h', 'h', 'anjst', 'wdnr']
note = ['h', 'ghq']
checkMagazine(magazine,note)
