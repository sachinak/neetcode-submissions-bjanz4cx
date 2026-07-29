class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        min_heap = []

        for x,y in points:
            d = (x)**2 + (y)**2
            heapq.heappush(min_heap, [d,x,y])
        res=[]
        while k>0:
            pt = heapq.heappop(min_heap)
            res.append([pt[1],pt[2]])        
            k-=1
        return res