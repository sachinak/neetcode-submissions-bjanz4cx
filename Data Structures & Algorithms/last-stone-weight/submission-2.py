class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-v for v in stones]
        heapq.heapify(arr)

        while len(arr) > 1:
            x = -heapq.heappop(arr)
            y = -heapq.heappop(arr)
            if x!=y:
                heapq.heappush(arr, -abs(x-y))
        return 0 if len(arr) == 0 else -arr[0]