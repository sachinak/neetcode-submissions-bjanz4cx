class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = [-1]*(len(heights))
        r = [-1]*(len(heights))
        stack = []
        n = len(heights)
        for idx, h in enumerate(heights):
            if not stack:
                stack.append(idx)
            else:
                while stack and h < heights[stack[-1]]:
                    l[stack[-1]] = idx - stack[-1]
                    stack.pop()
                else:
                    stack.append(idx)
        while stack:
            l[stack[0]] = len(stack)
            stack.pop(0)
        stack = []
        for ridx, h in enumerate(heights[::-1]):
            idx = n - ridx - 1
            
            if not stack:
                stack.append(idx)
            else:
                while stack and h < heights[stack[-1]]:
                    r[stack[-1]] = stack[-1] - idx 
                    stack.pop()
                else:
                    stack.append(idx)
        while stack:
            r[stack[0]] = len(stack)
            stack.pop(0)
        
        maxArea = -1

        for i in range(n):
            ta = heights[i]*(l[i] + r[i] - 1)
            maxArea = max(maxArea, ta)
        return maxArea