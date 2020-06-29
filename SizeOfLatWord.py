class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        print(len(s.split(' ')))
        print(s.split(' '))
        if len(s.split(' ')[len(s.split(' ')) - 1]) == 0:
            if len(s.split(' ')) == 2:
                return len(s.split(' ')[0])
            else:
                return 0
        else:
            if len(s.split(' ')) == 2:
                return len(s.split(' ')[1])
            else:
                return len(s.split(' ')[len(s.split(' ')) - 1])


print(Solution().lengthOfLastWord("I am a python Programer"))
print(Solution().lengthOfLastWord("I "))
