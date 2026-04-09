class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"]":"[", ")":"(", "}":"{"}
        for i in s:
            print(i, stack)
            if not stack:
                stack = [i] + stack
                continue
            if i in (')', '}', ']'):
                if d[i] == stack[0]:
                    stack.pop(0)
                else:
                    return False
            else:
                stack= [i] + stack
        if not stack:
            return True
        return False