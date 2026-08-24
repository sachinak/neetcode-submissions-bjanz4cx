class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n):
            for j in range(i+1,n):
                s[i],s[j] = s[j],s[i]
        
