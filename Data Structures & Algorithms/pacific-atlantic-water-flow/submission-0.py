class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pvis = set()
        avis = set()

        rows,cols = len(heights), len(heights[0])
       
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        def dfs(r,c, visited):
            if (r,c) in visited:
                return
            visited.add((r,c))
            for dr, dc in dirs:
                nr, nc = dr+r, dc+c

                if 0<= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)
           
        for r in range(rows):
            dfs(r,0, pvis)
            dfs(r,cols-1, avis)
        for c in range(cols):
            dfs(rows-1,c, avis)
            dfs(0,c, pvis)
       
            
            
        res = avis.intersection(pvis)
        return list(res)

