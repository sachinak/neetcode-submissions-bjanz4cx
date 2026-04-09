class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        for idx, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp, idx))
            else:
                i = 0
                # print(temp, stack)
                while stack and temp > stack[-1][0]:
                    t, idx2 = stack.pop()
                    i+=1
                    result[idx2] = idx - idx2
                stack.append((temp,idx))
        while stack:
            t, idx = stack.pop()
            result[idx] = 0
        return result