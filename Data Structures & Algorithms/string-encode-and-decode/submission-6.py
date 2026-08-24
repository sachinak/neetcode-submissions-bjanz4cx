class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        n = len(s)
        res = []
        i = 0
        
        ch = ""
        while i < n:
            if s[i] == "#":
                lenn = int(ch)
                
                st = s[i+1:i+1+lenn]
                res.append(st)
                i = i+1+lenn
                ch = ""
            else:
                ch += s[i]
                i+=1
            
        return res