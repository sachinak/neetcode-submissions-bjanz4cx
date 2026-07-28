class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]
        res = []
        def dfs(r):
            if r == n:
                cop = ["".join(row) for row in board]
                res.append(cop)
                return
            
            for c in range(n):
                i,j=r-1,c
                lc = True
                while i>=0:
                    if board[i][j] == 'Q':
                        lc = False
                        break
                    i-=1
                if not lc:
                    continue
                i,j=r-1,c-1
                rc = True
                while i>=0 and j>=0:
                    if board[i][j] == 'Q':
                        rc = False
                        break
                    i-=1
                    j-=1
                if not rc:
                    continue
                i,j=r-1,c+1
                cc = True
                while i>=0 and j<n:
                    if board[i][j] == 'Q':
                        cc = False
                        break
                    i-=1
                    j+=1
                if not cc:
                    continue
                
                board[r][c] = 'Q'
                dfs(r+1)
                board[r][c] = '.'
                


        dfs(0)
        print(res)
        return res
