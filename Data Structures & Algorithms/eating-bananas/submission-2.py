class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        mini = len(piles)
        mi = r
        while l <= r:
            m = (l+r)//2
            top = 0
            for p in piles:
                top += math.ceil(p/m)
            # print(l, r, m, top, mi)
            if top > h:
                l = m + 1
            elif top <= h:
                r = m - 1
                mi = m
            # if m < mi and top <= h:
            #     mini = top
            #     mi = m
        return mi
        