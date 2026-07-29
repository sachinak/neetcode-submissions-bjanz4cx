class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        
        visited = set()

        def dfs(u):            
            for v in adj[u]:
                if v not in visited:
                    visited.add(v)
                    dfs(v)

        res = []
        ctr = 0
        for u in range(n):
            if u not in visited:
                visited.add(u)
                dfs(u)
                ctr+=1
            
       
        return ctr
