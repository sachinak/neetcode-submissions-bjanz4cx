class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        v = [[x*x+y*y, x, y] for x,y in points]
        heapq.heapify(v)

        res = []
        while k > 0:
            d, px, py = heapq.heappop(v)
            res.append([px, py])
            k-=1
        return res