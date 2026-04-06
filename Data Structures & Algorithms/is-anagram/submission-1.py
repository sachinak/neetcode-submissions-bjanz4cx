class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = Counter(s)
        tt = Counter(t)

        for i in ss:
            if ss[i] != tt[i]:
                return False
        for i in tt:
            if ss[i] != tt[i]:
                return False
        return True