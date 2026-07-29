class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        if n == 2:
            if s == s[::-1]:
                return s
            else:
                return s[1]
        res = -1
        resLen = 0
        #odd
        for i in range(n):
            l,r=i-1,i+1
            flag = False
            while l >= 0 and r < n and s[l] == s[r]:
                l-=1
                r+=1
                flag = True
            if flag:
                l+=1
                r-=1
                # print(l, r, i)
                if r - l + 1 > resLen:
                    res = l
                    resLen = r - l + 1
        
        #even
        for i in range(n):
            l,r=i,i+1
            while l >= 0 and r < n and s[l] == s[r]:
                l-=1
                r+=1
                flag = True
            if flag:
                l+=1
                r-=1
                
                if r - l + 1 > resLen:
                    res = l
                    resLen = r - l + 1

        return s[res:res+resLen]