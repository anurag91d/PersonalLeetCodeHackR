def reverseString(s):
    # return str[::-1]
    i = len(s) - 1
    while i >= 0:
        print(s[i], end=" ")
        i -= 1


s = "I am fluxraiser"
reverseString(s)
