class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        res = set()
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] == 'X' or (i,j) in res:
                return
            res.add((i, j))
            dfs(i+1, j)
            dfs(i-1,j)
            dfs(i, j+1)
            dfs(i,j-1)
       

        for i in range(rows):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][cols-1] == 'O':
                dfs(i, cols-1)
        
        for j in range(cols):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[rows-1][j] == 'O':
                dfs(rows-1,j)
        
        
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in res and board[i][j] == 'O':
                    board[i][j] = 'X'
        