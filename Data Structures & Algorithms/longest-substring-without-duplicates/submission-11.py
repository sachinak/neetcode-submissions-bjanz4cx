class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        l = 0
        r = 1
        cnt = 1
        d = {s[l]:l}
        while r < len(s):
            
            if s[r] in d:
                l = max(d[s[r]]+1, l)
                
            d[s[r]] = r
            r+=1
            cnt = max(cnt, r - l)
                
        return cnt