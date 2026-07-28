class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"],
        }
        res = []
        
        
        def dfs(idx, s):
            if len(s) == len(digits):
                res.append(s)
                return
            
            for k in mapping[digits[idx]]:
                dfs(idx+1, s+k)
                

        if digits:  
            dfs(0,"")
        return res