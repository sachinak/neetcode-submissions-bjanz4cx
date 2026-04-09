class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if s == t:
            return s
        
        c1 = Counter(t)

        minLen = len(s) + 1
        minS = ""
        l = 0
        lt = len(t)
        ol = l
        flag2= False
        for i in range(len(t),len(s)+1):
            temp = s[l:i]
            # print(l, i, temp)
            
            c2 = Counter(temp)
            flag = True
            while flag:
                for c in c1:
                    if c2.get(c,0) < c1.get(c):
                        flag = False
                        break
                if not flag:
                    break
                
                if minLen > i - l + 1:
                    minLen = i - l + 1
                    ol = l
                flag2= True
                
                l+=1
                temp = s[l:i]
                c2 = Counter(temp)
                
                print("in",l, i, temp, minLen)
        if not flag2:
            return ""   
        # print(ol, minLen)
        return s[ol:ol+minLen-1]

        