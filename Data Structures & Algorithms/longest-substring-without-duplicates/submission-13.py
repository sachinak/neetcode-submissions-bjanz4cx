class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0
        cnt = 0
        d = {}
        while r < len(s):
            
            if s[r] in d:
                l = max(d[s[r]]+1, l)
                
            d[s[r]] = r
            r+=1
            cnt = max(cnt, r - l)
                
        return cnt