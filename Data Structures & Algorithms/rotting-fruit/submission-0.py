class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        time = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.pop(0)

                for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                    nr = r+dr
                    nc = c+dc
                    if nr >=0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh-=1
                        q.append((nr, nc))
            time+=1
        return time if fresh == 0 else -1