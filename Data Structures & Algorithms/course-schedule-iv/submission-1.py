class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        g = {idx:[] for idx in range(numCourses)}

        for u,v in prerequisites:
            g[v].append(u)
        
        
        def dfs(u):
            for v in g[u]:
                if v not in visited:
                    visited.add(v)
                    dfs(v)
        preQMap = {}
        for i in range(numCourses):
            visited = set()
            if i not in visited:
                dfs(i)
            preQMap[i] = visited
        ans = []
        print(preQMap)
        for u, v in queries:
            if u in preQMap[v]:
                ans.append(True)
            else:
                ans.append(False)
        return ans

       