class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)

        max_heap = [-cnt for cnt in c.values()]
        q = deque()
        time = 0
        heapq.heapify(max_heap)

        while max_heap or q:
            time += 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt != 0:
                    q.append([cnt, time+n])
            else:
                time = q[0][1]
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time