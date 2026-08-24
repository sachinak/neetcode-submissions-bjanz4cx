class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        colss= []
        for i in range(rows):
            t = []
            for j in range(cols):
                t.append(board[j][i])
            colss.append(t)
        
        sq = []
        cnt = 0
        while cnt < 81:
            ix = 3*(cnt//27)
            t = []
            jj = (cnt%27)//9
            for i in range(ix, ix+3):
                jx = jj*3
                for j in range(jx, jx+3):
                    
                    t.append(board[i][j])
                    cnt+=1
            jj+=1
            sq.append(t)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j]!= '.':
                    if board[i].count(board[i][j]) > 1:
                        return False
                    if colss[j].count(board[i][j]) > 1:
                        return False
    
                    if sq[(i//3)*3+(j//3)].count(board[i][j]) > 1:
                        return False
        return True 
                