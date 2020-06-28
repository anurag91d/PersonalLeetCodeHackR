def bsearch(nums, item):
    low = 0
    high = len(nums) - 1
    # print(low,high)
    while low <= high:
        mid = int((high + low) // 2)
        # print(mid)
        if item == nums[mid]:
            return mid + 1
        if item > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if low > high:
        return None


nums = [1, 4, 6, 8, 9, 12, 56, 77, 98, 111, 444, 500]
print(bsearch(nums, 12))
print(bsearch(nums, 111))
print(bsearch(nums, 1))
print(bsearch(nums, 400))
print(bsearch(nums, 500))
