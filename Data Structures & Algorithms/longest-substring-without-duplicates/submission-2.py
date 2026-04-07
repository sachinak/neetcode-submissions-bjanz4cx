class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        l = 0 
        r = 1
        d = defaultdict()
        n = len(s)
        maxLen = 1
        d[s[l]] = l
        while r < n:
            # print(l, r, s[l], s[r], maxLen, d, d.get(s[r]))
            if d.get(s[r]) != None:
                l = d[s[r]]+1
                r = l+1
                d = defaultdict()
                d[s[l]] = l
            else:
                d[s[r]] = r
                maxLen = max(maxLen, r-l+1)
                r+=1
                
        return maxLen