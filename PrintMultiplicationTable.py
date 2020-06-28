
def printTable(n):
    i = 1
    for i in range(1,n+1):
        j = 1
        for j in range(1,n+1):
            print(i * j, end = "\t")
        print("")


printTable(12)