class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < 0 or len(b) > 10 ** 4:
            return "Invalid Input"
        else:
            integer_sum = int(a, 2) + int(b, 2)
            binary_sum = bin(integer_sum)
            res = str(binary_sum)
            return res[2:]


print(Solution().addBinary("11", "1"))
