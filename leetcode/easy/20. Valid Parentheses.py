class Solution(object):
    def isValid(self, s):
        stack = []
        parenth = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for i in s:
            if i in parenth:
                stack.append(i)
            else:
                if stack and parenth[stack.pop()] == i:
                    continue
                else:
                    return False

        return not stack
