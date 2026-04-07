class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cc = {}
        maxF = 0
        l = 0
        res = 0
        for i in range(len(s)):
            cc[s[i]] = 1 + cc.get(s[i], 0)
            maxF = max(maxF, cc[s[i]])

            while (i - l + 1) - maxF > k:
                cc[s[l]] -= 1
                l+=1
            res = max(res, i - l + 1)
        return res