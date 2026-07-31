class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n<0:
            x=1/x
        res = x
        i = 0
        while i < abs(n)-1:
            
            res*=x
            i+=1
        return res
       