# https://leetcode.com/problems/palindrome-number/

# Runtime: 72 ms, faster than 35.77% of Python3 online submissions for Palindrome Number.
# Memory Usage: 14.2 MB, less than 76.68% of Python3 online submissions for Palindrome Number.
def isPalindrome(x: int) -> bool:
    number = x
    if number < 0:
        number *= -1
    reversedNumber = 0
    while number > 0:
        reversedNumber = (reversedNumber * 10) + (number % 10)
        number = int(number / 10)

    if x == reversedNumber:
        return True
    return False

print(isPalindrome(123))
print(isPalindrome(-123))
print(isPalindrome(121))
print(isPalindrome(-121))

# Second approach using stack. This approach takes more time compared to the above approach.
# Runtime: 80 ms, faster than 24.04% of Python3 online submissions for Palindrome Number.
# Memory Usage: 14.2 MB, less than 48.53% of Python3 online submissions for Palindrome Number.
def isPalindrome2(x: int) -> bool:
    numberInString = str(x)
    stack = []
    mid = int(len(numberInString) / 2)

    for i in range(mid):
        stack.append(numberInString[i])

    popIndex = mid
    if len(numberInString)%2 != 0:
        popIndex = mid+1

    for i in range(popIndex, len(numberInString)):
        pop = stack.pop()
        if pop != numberInString[i]:
            return False
    return True

print(isPalindrome2(123))
print(isPalindrome2(-123))
print(isPalindrome2(121))
print(isPalindrome2(-121))

