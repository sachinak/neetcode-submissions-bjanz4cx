class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        d= [-c[k] for k in c]
        q=deque()
        heapq.heapify(d)
        time = 0
        while d or q:
            time+=1

            if d:
                cnt = 1 + heapq.heappop(d)
                if cnt != 0:
                    q.append([cnt, time+n])
            else:
                time = q[0][1]
            if q and q[0][1] == time:
                heapq.heappush(d, q.popleft()[0])
        return time
        