class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-v for v in nums]
        heapq.heapify(nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        heapq.heapify(self.nums)
        k = self.k

        res =[]
        while k:
            ele = heapq.heappop(self.nums)
            res.append(ele)
            k-=1
            # print(ele, k)
        while res:
            heapq.heappush(self.nums, res.pop())
        
        return -ele

