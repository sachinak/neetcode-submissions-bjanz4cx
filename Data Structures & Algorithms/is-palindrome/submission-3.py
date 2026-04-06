class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        res = ""
        for i in s:
            if i.isalnum():
                if i.isalpha:
                    res+=i.lower()
                else:
                    res+=i
        l = 0
        r = len(res) -1
        if res == "":
            return True
        
        while l < r:
            if res[l] != res[r]:
                return False
            l+=1
            r-=1
        return True