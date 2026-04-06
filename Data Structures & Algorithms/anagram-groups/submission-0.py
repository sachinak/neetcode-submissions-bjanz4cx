class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ss = {}
        for s in strs:
            sos = "".join(sorted(s))
            if sos in ss:
                ss[sos].append(s)
            else:
                ss[sos] = [s]
        # print(ss.values())
        return list(ss.values())