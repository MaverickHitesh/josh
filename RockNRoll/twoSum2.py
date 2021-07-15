def twoSum2(nums: [int], target: int) -> [int]:
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left]+nums[right] > target:
            right -= 1
        elif nums[left]+nums[right] < target:
            left += 1
        else:
            return [left, right]
    return

print(twoSum2([2,7,11,15], 9))
print(twoSum2([1,2,7,11,15], 9))
print(twoSum2([1,2,3,7,11,15], 10))

