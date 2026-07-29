class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = {}
        indeg = {}
        for u in range(numCourses): 
            adj[u] = []
            indeg[u] = 0
        for u, v in prerequisites: 
            adj[v].append(u)
            indeg[u] += 1
        q = deque()

        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)

        res = []    
        while q:
            u = q.popleft()
            res.append(u)
            for v in adj[u]:
                indeg[v]-=1
                if indeg[v] == 0:
                    q.append(v)
        
        if len(res) == (numCourses):
            return res
        return []
        