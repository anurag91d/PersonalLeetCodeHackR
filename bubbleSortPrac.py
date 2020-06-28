def bubble(nums):

    i = 0
    j =0
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums [j+1]:
                t = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = t
    return nums

nums = [0, 14, 26, 83, 99, 1244, 50, 2, 98, 111, 44, 5]
print(bubble(nums))
nums.sort()
print(nums)
