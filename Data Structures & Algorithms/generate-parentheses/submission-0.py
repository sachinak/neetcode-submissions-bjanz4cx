class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        res = set()
        self.s = ""
        def rec(op, cl):
            if op > n or cl > n:
                return
            if len(self.s) == 2*n:
                res.add(self.s)
                return
            
            if cl > op:
                return
            
            
            self.s+="("
            rec(op+1, cl)
            self.s = self.s[:-1]
            self.s += ")"
            rec(op, cl+1)
            self.s = self.s[:-1]
        rec(0,0)
        return list(res)

