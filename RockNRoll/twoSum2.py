# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Runtime: 60 ms, faster than 85.59% of Python3 online submissions for Two Sum II - Input array is sorted.
# Memory Usage: 14.8 MB, less than 32.26% of Python3 online submissions for Two Sum II - Input array is sorted.
def twoSum2(nums: [int], target: int) -> [int]:
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left]+nums[right] > target:
            right -= 1
        elif nums[left]+nums[right] < target:
            left += 1
        else:
            return [left+1, right+1]
    return

print(twoSum2([2,7,11,15], 9))
print(twoSum2([1,2,7,11,15], 9))
print(twoSum2([1,2,3,7,11,15], 10))

