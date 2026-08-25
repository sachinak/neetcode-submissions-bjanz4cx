class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for ch in s:
            if not stack:
                stack.append(ch)
                continue
            if ch in ['(','[','{']:
                stack.append(ch)
            else:
                if stack and ch == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                if ch == '}':
                    if stack and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                if ch == ']':
                    if stack and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                
        return False if stack else True