class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}
        def rec(i,j):
            k = i+j
            if k == len(s3):
                return (i == len(s1)) and (j==len(s2))
            if (i,j) in dp:
                return dp[(i,j)]
            if i < len(s1) and s1[i] == s3[k]:
                if dp.get((i+1,j)):
                    return dp.get((i+1,j))
                dp[(i+1, j)] = rec(i+1, j)
                if dp[(i+1, j)]:
                    return True
            if j < len(s2) and s2[j] == s3[k]:
                if dp.get((i,j+1)):
                    return dp.get((i,j+1))
                dp[(i,j+1)] = rec(i, j+1)
                if dp[(i, j+1)]:
                    return True
            dp[(i,j)] = False
            return dp[(i,j)]
            
            
        return rec(0, 0)
        