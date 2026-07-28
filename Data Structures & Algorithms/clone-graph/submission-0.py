"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        d = {}
        visited = {}
        if not node:
            return None
        def dfs(root):
            visited[root.val] = True
            
            for v in root.neighbors:
                
                if d.get(root.val):
                    d[root.val].append(v.val) 
                else:
                    d[root.val] = [v.val]
                if visited.get(v.val) and visited[v.val]: continue
                dfs(v)

        dfs(node)
        k = {}
        for i in range(len(visited)):
            k[i+1] = Node(i+1)
        for key in d:
            for v in d[key]:
                k[key].neighbors.append(k[v])
        
        return k[1]