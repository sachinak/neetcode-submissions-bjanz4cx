class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for u,v in prerequisites:
            adj[u].append(v)
        
        final = set()
        def dfs(u):
            if u in visited:
                return False
            if u in final:
                return True
            visited.add(u)
            for v in adj[u]:
                if not dfs(v):
                    return False
            final.add(u)
            visited.remove(u)
            return True
        visited = set()
        for u in adj:
            
            if not dfs(u):
                return False
        return True
            