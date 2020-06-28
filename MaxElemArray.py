from array import *


def Largest(arr):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    print(max)


def reverseList(arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        t = arr[low]
        arr[low] = arr[high]
        arr[high] = t
        low += 1
        high -= 1
    print(arr)


def sub_lists(list1):
    # store all the sublists
    sublist = [[]]

    # first loop
    for i in range(len(list1) + 1):

        # second loop
        for j in range(i + 1, len(list1) + 1):
            # slice the subarray
            sub = list1[i:j]
            sublist.append(sub)

    return sublist


def matrixprint(mat):
    for i in range(len(mat) - 1, 0, -1):
        print(mat[i])


def removeduplicates(arr):
    i = 0
    print(list(set(arr)))
    print(arr, end="YO")


arr = [1, 3, 5, 2, 111111, 7, 8, 8, 8, 9, 3, 999, 0, 32, 554, 999]
Largest(arr)
reverseList(arr)
string = "abcde"
sublist = sub_lists(arr)
# matrixprint(sub_lists(arr))
print(sub_lists(string))
# matrixprint(sub_lists(string))
removeduplicates(arr)
