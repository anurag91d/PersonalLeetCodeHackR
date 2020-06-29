import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        test =""
        if len(s) == 0:
            return True
        s = s.casefold()
        for i in s:
            if(re.findall("[0-9a-z]", i)):
                test = test + i
        print(test)
        if test == test[::-1]:
            return True
        else:
            return False
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome("0P"))

