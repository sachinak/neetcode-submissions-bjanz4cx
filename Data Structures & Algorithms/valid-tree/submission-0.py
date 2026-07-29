class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        visiting = set()
        res = []
        
        def dfs(u,p):
            if u in visited:
                return True
            if u in visiting:
                return False
            print(u)
            visiting.add(u)
            for v in adj[u]:
                if v == p:
                    continue
                if not dfs(v, u):
                    return False
            visiting.remove(u)
            visited.add(u)
            res.append(u)
            return True

        
        if not dfs(0,-1):
            return False

        if len(res) != n:
            return False
        
        return True