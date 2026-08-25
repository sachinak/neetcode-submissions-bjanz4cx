class MinStack:

    def __init__(self):
        self.stack = deque()
        self.q = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.q, val)

    def pop(self) -> None:
        v=self.stack.pop()
        self.q.remove(v)
        heapq.heapify(self.q)
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        
        return self.q[0]