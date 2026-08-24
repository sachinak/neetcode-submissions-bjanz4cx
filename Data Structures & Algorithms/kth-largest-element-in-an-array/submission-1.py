class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [-v for v in nums]
        heapq.heapify(arr)

        while k > 0:
            res = heapq.heappop(arr)
            k-=1
        return -res