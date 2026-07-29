class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        
        visited = set()

        def dfs(u, p):
            if u in visited:
                return
            visited.add(u)
            
            for v in adj[u]:
                if v == p:
                    continue
                
                dfs(v, u)
                


        res = []
        ctr = 0
        for u in range(n):
            
            if u in visited:
                continue
            ctr+=1
            dfs(u, -1)
            
       
        return ctr
