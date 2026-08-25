class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        for a in arr:
            res.append(abs(x-a))
        res = [[v,i] for i, v in enumerate(res)]
        res.sort()
        # return [arr[res[0][1]], arr[res[1][1]]]
        ans = []
        for i in range(k):
            ans.append(arr[res[i][1]])
        return sorted(ans)