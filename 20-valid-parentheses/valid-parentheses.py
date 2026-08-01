class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if i in '([{':
                stack.append(i)
            elif i in ')]}':
                if not stack:
                    return False
                top = stack.pop()
                if (top == '(' and i != ')') or (top == '{' and i != '}') or (top == '[' and i != ']'):
                    return False 
        return not stack
        