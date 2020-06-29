import array as arr

class Solution(object):
    def majorityElement(self, nums):
        map = dict({})
        max = nums[0]
        for key in nums:
            map[key] = map.get(key, 0) + 1
            if map[key] > map[max]:
                max =key
        return max



nums = arr.array("i",[1,2,4,2,2,2,6,6,6,6,6,7])
print(Solution().majorityElement(nums))
