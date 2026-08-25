class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        l1 = len(s1)
        c2 = Counter(s2[:l1])
        cnt = 0
        
        if c1 == c2:
            return True
       
        for i in range(1, len(s2) - l1+1):
            
            c2[s2[i+l1 - 1]] += 1
            c2[s2[i - 1]] -= 1
            
            if c1 == c2:
                return True
            
        return False