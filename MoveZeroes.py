import array as arr
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            flag = -1
            for i in range(len(nums)):
                if nums[i] == 0:
                    if flag > i:
                        j = flag
                    else:
                        j = i+1
                    while j<len(nums) and nums[j] == 0:
                        j += 1
                    if j == len(nums) or nums[j] == 0:
                        break
                    else:
                        nums[i], nums[j] = nums[j], nums[i]
                        flag = j
                        # j += 1
        print(nums)
        return None

# class Solution:
#     def moveZeroes(self, nums):
#         """Do not return anything, modify nums in-place instead"""
#         print(nums)
#         i = 0
#         while i < len(nums):
#             if nums[i] == 0:
#                 nums.remove(nums[i])
#                 nums.append(0)
#             i +=1
#         print(nums)
#         return None


s1 = Solution()
nums = arr.array("i", [1, 2, 4, 0, 2, 9, 6, 0, 0, 64, 60, 70])
s1.moveZeroes(nums)
