class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        mull = []
        
        for ch in s:
            if not stack:
                stack.append(ch)
            else:
                v = ""
                if ch == "[":
                    
                    while stack and stack[-1].isdigit():
                        v+=stack.pop()
                    mull.append(int(v[::-1]))
                    stack.append(ch)
                elif ch == "]":
                    cur = []
                    while stack[-1] != "[":
                        cur.append(stack.pop())
                    
                    if stack[-1] == "[": stack.pop()
                    v = 1
                    if mull:
                        v = mull.pop()
                    print(cur, stack)
                    cur = cur[::-1]
                    cur = "".join(cur)
                    print(cur, stack)
                    stack.append(cur*v)
                    
                else:
                    stack.append(ch)
        return "".join(stack)