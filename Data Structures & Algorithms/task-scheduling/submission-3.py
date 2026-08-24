class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        cc = [-cnt for cnt in c.values()]
        q = deque()
        heapq.heapify(cc)
        time = 0
        while cc or q:
            time+=1
            if cc:
                cnt = 1 + heapq.heappop(cc)
                if cnt != 0:
                    q.append([cnt, time+n])
            else:
                time = q[0][1]
            if q and q[0][1] == time:
                heapq.heappush(cc, q.popleft()[0])
        return time