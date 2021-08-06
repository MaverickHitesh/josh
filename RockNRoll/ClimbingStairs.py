# https://leetcode.com/problems/climbing-stairs

# Runtime: 32 ms, faster than 51.86% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 14.3 MB, less than 44.36% of Python3 online submissions for Climbing Stairs.
def climbStairs(n: int) -> int:
    one = 1
    two = 1

    for i in range(n-1):
        temp = one
        one = one + two
        two = temp

    return one

print(climbStairs(3))
print(climbStairs(2))
print(climbStairs(5))
