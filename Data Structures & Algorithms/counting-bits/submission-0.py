class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = [0 for i in range(n+1)]
        for idx in range(len(res)):
            res[idx] = bin(idx).count('1')
        
        return res