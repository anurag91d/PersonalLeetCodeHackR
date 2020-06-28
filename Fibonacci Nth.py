#!/usr/bin/env python3.8
# 0 1 1 2 3 5 8 13 21 34 55 89 144

def Fibo(n):
    count = 3
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        i = 0
        j = 1
        while count <= n:
            num = i + j
            i = j
            j = num
            count += 1
            print(num)
        return num


def recur_fibo(n):
    count = 0
    i = 0
    j = 1
    if n == 1:
        return i
    else:
        n = i+j
        i = j
        j = n
        print(n)
        count +=1
        if count == n:
            return "end"
        else:

            return (recur_fibo(i,j))


        # return (recur_fibo(n - 1) + recur_fibo(n - 2))


nterms = 10

# check if the number of terms is valid

print("Fibonacci sequence:")
# for i in range(nterms):
print(recur_fibo(nterms))

# print(Fibo(10))
