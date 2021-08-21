# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

def maxSubArray(nums: [int]) -> int:
    maxSum = nums[0]
    curSum = 0

    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSum = max(maxSum, curSum)

    return maxSum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))