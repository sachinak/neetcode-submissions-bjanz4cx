class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack = [val] + self.stack

    def pop(self) -> None:
        self.stack.pop(0)

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return min(self.stack)
