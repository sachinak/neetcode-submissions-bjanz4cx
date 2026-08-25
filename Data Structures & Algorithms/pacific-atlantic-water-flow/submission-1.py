class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        
        
        avis = set()
        pvis = set()
        def dfs(x, y, res):
            if (x,y) in res:
                return 
            res.add((x,y))
            
            for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                nx, ny = x+dx, y+dy
                if 0<=nx<rows and 0<=ny<cols and heights[nx][ny] >= heights[x][y]:
                    dfs(nx,ny, res)
            
        
        
        for i in range(rows):
            dfs(i, 0, pvis)
            dfs(i, cols-1, avis)
        for j in range(cols):
            dfs(0, j, pvis)
            dfs(rows-1, j, avis)

        return list(avis.intersection(pvis))

