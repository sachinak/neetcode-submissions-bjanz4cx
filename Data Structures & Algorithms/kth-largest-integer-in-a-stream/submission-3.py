class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = [-v for v in nums]
        
        heapq.heapify(self.arr)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.arr, -val)
        cnt = self.k
        res = []
        
        while cnt > 0:
            
            v = heapq.heappop(self.arr)
           
            res.append(v)
            cnt-=1
        
        for r in res:
            heapq.heappush(self.arr, r)
        return -v
        
