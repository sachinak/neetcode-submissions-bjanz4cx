class Solution:
    def validPalindrome(self, s: str) -> bool:
        def pali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return (pali(l, r - 1) or pali(l+1, r))
            l+=1
            r-=1
        return True