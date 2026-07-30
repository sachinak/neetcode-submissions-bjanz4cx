class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1,n+1)}
        for u, v, w in times:
            adj[u].append((v, w))
        
        visited = set()
        dist = [float('inf')]*(n+1)
        
        q =[[0,k]]
        t = 0 
        print(adj)
        while q:
            cost, cur = heapq.heappop(q)
            if cur in visited:
                continue
            visited.add(cur)
            t = cost
            for v, new_cost in adj[cur]:
                if v not in visited:
                    heapq.heappush(q, (cost+new_cost, v))
        return t if len(visited) == n else -1