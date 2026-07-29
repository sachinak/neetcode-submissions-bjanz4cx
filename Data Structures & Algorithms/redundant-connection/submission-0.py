class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        adj = [[] for _ in range(n+ 1)]
        indeg = [0]*(n+1)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indeg[v]+=1
            indeg[u]+=1
        
        q = deque()

        for i in range(n+1):
            if indeg[i] == 1:
                q.append(i)
        
        while q:
            u = q.popleft()
            indeg[u] -=1
            for v in adj[u]:
                indeg[v] -=1
                if indeg[v] == 1:
                    q.append(v)
        
        for u, v in reversed(edges):
            if indeg[u] > 0 and indeg[v] > 0:
                return [u,v]

        return []