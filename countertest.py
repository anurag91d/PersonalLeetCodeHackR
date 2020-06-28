from collections import Counter

#!/bin/python

import math
import os
import random
import re
import sys
import collections

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    c1 = collections.Counter(a)
    c2 = collections.Counter(b)
    # for
    c3 = c2 - c1
    c4 = c1 - c2
    c5 = c3 + c4
    print(c1)
    print(c2)
    print(c5)
    print(sum(c5.values()))

    return len(c5)
a ="abcdefghijkl"
b ="abrtyuuu"
res = makeAnagram(a, b)
