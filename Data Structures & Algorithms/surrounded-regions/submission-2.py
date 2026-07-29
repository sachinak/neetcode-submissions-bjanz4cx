class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows, cols = len(board), len(board[0])
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(r,c,safe):
            if r < 0 or r >= rows or c <0 or c >= cols or board[r][c] == 'X' or (r,c) in safe:
                return
            
            safe.add((r,c))
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if nr >=0 and nr < rows and nc >= 0 and nc < cols and board[nr][nc] != 'X':
                    dfs(nr, nc, safe)

        safe = set()
        for c in range(cols):
            dfs(0, c, safe)
            dfs(rows-1, c, safe)
        for r in range(rows):
            dfs(r, 0, safe)
            dfs(r, cols-1, safe)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r,c) not in safe:
                    board[r][c] = 'X'