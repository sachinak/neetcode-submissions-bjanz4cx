class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0

        stack = []

        for token in tokens:
            if token not in ["+", "-", "/", "*"]:
                stack = [int(token)] + stack
            else:
                a = stack.pop(0)
                b = stack.pop(0)
                
                if token == "+":
                    res = a + b
                elif token == "-":
                    res = b-a
                elif token == "*":
                    res = a*b
                elif token == "/":
                    res = int(float(b)/a)
                
                stack = [res] + stack
                
        return stack[0]

