# https://leetcode.com/problems/valid-parentheses/

# Runtime: 28 ms, faster than 86.02% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14.4 MB, less than 7.32% of Python3 online submissions for Valid Parentheses.
def isValid(s: str) -> bool:
    stack = []
    for c in s:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            else:
                pop = stack.pop()
                if pop == '(' and c == ')':
                    continue
                elif pop == '{' and c == '}':
                    continue
                elif pop == '[' and c == ']':
                    continue
                else:
                    return False
    if len(stack) == 0:
        return True
    else:
        return False
print("---- method 1 ----")
print(isValid("({[]})"))
print(isValid("({]})"))
print(isValid("({[])"))
print("------")
print(isValid("({[}])"))
print(isValid("()"))

# Runtime: 32 ms, faster than 65.68% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14.3 MB, less than 63.46% of Python3 online submissions for Valid Parentheses.
def isValid2(s: str) -> bool:
    stack = []
    dict = {"]": "[", "}": "{", ")": "("}
    for c in s:
        if c in dict.values():
            stack.append(c)
        elif c in dict.keys():
            if len(stack) == 0 or dict[c] != stack.pop():
                return False
        else:
            return  False

    return stack == []
print("---- method 2 ----")
print(isValid2("({[]})"))
print(isValid2("({]})"))
print(isValid2("({[])"))
print("------")
print(isValid2("({[}])"))
print(isValid2("()"))