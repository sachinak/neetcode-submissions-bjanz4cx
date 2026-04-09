class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        l1 = len(s1)
        c2 = Counter(s2[:l1])
        cnt = 0
        for c in c2:
            if c1.get(c) == c2[c]:
                cnt+=1
        if c1 == c2:
            return True
        # print(c1, c2, cnt)
        for i in range(1, len(s2) - l1+1):
            # print(s2[i+l1 - 1], s2[i-1])
            
            c2[s2[i+l1 - 1]] += 1
            c2[s2[i - 1]] -= 1
            if c1.get(s2[i]) == c2[s2[i]]:
                cnt += 1
            if c1 == c2:
                return True
            # print(c2, cnt)
            
        return False