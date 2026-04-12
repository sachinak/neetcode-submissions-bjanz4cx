class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l = []
        for i in range(len(position)):
            l.append([position[i], speed[i]])
        l.sort(key=lambda x:x[0], reverse=True)
    
        k = []

        for i in range(len(position)):
            t = (target - l[i][0])/l[i][1]
            k.append(t)
        
        fl = set()

        stack = []
        for ti in k:
            if not stack:
                stack.append(ti)
            else:
                if stack[-1] >= ti:
                    fl.add(ti)
                else:
                    stack.append(ti)
        return len(stack)
