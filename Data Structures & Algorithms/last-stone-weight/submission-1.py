class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        q = [-v for v in stones]
        heapq.heapify(q)
        while q and len(q) > 1:
            a = -heapq.heappop(q)
            b = -heapq.heappop(q)
            if a != b:
                heapq.heappush(q, -abs(a-b))
        
        return -q[0] if q else 0