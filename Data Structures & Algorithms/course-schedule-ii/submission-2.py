class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = {}
        for u in range(numCourses): adj[u] = []
        for u, v in prerequisites: adj[u].append(v)

        visited = set()
        visiting = set()
        res = []

        def dfs(u):
            if u in visited:
                
                return True
            if u in visiting:
                return False
            visiting.add(u)
            for v in adj[u]:
                if not dfs(v):
                    return False
            visiting.remove(u)
            visited.add(u)
            res.append(u)
            return True
        

        for u in range(numCourses):
            if not dfs(u):
                return []
        
        return res