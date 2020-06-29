class Solution(object):
    def reverse(self, x: int) -> int:
        rev = int(0)
        k = 0
        if x < 0:
            k = 1
            x = -x
        while x != 0:
            print(x)
            rev = rev * 10 + (x % 10)
            x=int(x/10)
        if k ==0:
            if(abs(rev) > (2 ** 31 - 1)):
                return 0
            else:
                return rev
        else:
            if(abs(rev) > (2 ** 31 - 1)):
                return 0
            else:
                return -rev

print(Solution().reverse(123))
print(Solution().reverse(-123))
print(Solution().reverse(1534236469))

