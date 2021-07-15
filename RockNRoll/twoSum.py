# https://leetcode.com/problems/two-sum/
def twoSum(nums: [int], target: int) -> [int]:
    previousMap = {}  # val: index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in previousMap:
            return [previousMap[diff], i]
        previousMap[n] = i

print(twoSum([2,7,11,15], 9))
print(twoSum([1,2,7,11,15], 9))
print(twoSum([1,2,3,7,11,15], 10))