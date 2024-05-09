def ValidParenthesis(s:str):
    stack = []
    parenthesis = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in parenthesis.values():
            stack.append(char)
        elif char in parenthesis:
            if not stack or stack.pop() != parenthesis[char]:
                return False
        else:
            pass
    return not stack

print("Test_Case1",ValidParenthesis("()[]{}"))
print("Test_Case2",ValidParenthesis("()"))
print("Test_Case3",ValidParenthesis("(]"))