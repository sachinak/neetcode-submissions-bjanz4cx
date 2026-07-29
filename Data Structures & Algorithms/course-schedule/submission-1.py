class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for u,v in prerequisites:
            adj[u].append(v)
        
        
        def dfs(u):
            if u in visited:
                return False
            if adj[u] == []:
                return True
            visited.add(u)
            for v in adj[u]:
                if not dfs(v):
                    return False
            visited.remove(u)
            return True
        visited = set()
        for u in adj:
            
            if not dfs(u):
                return False
        return True
            