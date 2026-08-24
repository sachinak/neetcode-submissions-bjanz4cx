class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs[0] == "":
            return ""
        if "" in strs:
            return ""
        a = strs[0][0]
        
           
        i= 1
        while True:
            for s in strs[1:]:
                if len(s) < i:
                    return a[:i-1]
                
                if s[:i] != a:
                    return s[:i-1]
            i+=1
            if i > len(strs[0]):
                return a
            a += strs[0][i-1]
        