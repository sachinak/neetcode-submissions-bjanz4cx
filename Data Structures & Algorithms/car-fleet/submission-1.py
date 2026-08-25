class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = [[idx, pos] for idx, pos in enumerate(position)]
        res.sort(reverse=True, key= lambda x: x[1])

        stack = []
        for i, p in res:
            t = (target-p)/speed[i]

            stack.append(t)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack) 