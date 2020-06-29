class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        check = x
        rev = int(0)
        while x > 0:
            rev = rev * 10 + x % 10
            x = int(x/10)
        if check == rev:
            return True
        else:
            return False


print(Solution().isPalindrome(121))
print(Solution().isPalindrome(123))
print(Solution().isPalindrome(-121))
