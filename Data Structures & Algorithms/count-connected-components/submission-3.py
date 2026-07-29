class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        
        visited = set()
        visiting = set()
        def dfs(u, p, temp):
            if u in temp:
                return
            visited.add(u)
            temp.append(u)
            
            for v in adj[u]:
                if v == p:
                    continue
                
                dfs(v, u, temp)
                


        res = []
        for u in range(n):
            temp = []
            if u in visited:
                continue
            dfs(u, -1, temp)
            res.append(temp)
       
        return len(res)
