# https://leetcode.com/problems/reverse-integer/
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

def reverse(num: int) -> int:
    number = num
    if number < 0:
        number *= -1
    reversedNumber = 0
    while number > 0:
        reversedNumber = (reversedNumber*10) + (number%10)
        number = int(number / 10)
        if not (abs(reversedNumber) < 2**31 and reversedNumber != 2**31 - 1):
            # If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
            return 0

    if num < 0:
        reversedNumber *= -1
    return reversedNumber

print(reverse(123))
print(reverse(-123))
print(reverse(1534236469))

