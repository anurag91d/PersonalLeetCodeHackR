import os
import sys

def addIntegers():
    sum = 0
    infile = open("Integers", "r")
    for num in infile:
        sum = sum + int(num)
    print(sum)

# os.system("ls")
addIntegers()


