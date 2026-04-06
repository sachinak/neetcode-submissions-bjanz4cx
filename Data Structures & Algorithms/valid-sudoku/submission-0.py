class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dabbe = [set(),set(),set(),set(),set(),set(),set(),set(),set()]
        for i in range(9):
            k = set()
            k2 = set()
            for j in range(9):
                if board[i][j] in k:
                    return False
                if board[i][j].isdigit():
                    k.add(board[i][j])
                if board[j][i] in k2:
                    return False
                if board[j][i].isdigit():
                    k2.add(board[j][i])

                ix = (i//3)*3+j//3
                k3 = dabbe[ix]
                if board[i][j] in k3:
                    return False
                if board[i][j].isdigit():
                    k3.add(board[i][j])
        # print(dabbe)
        return True
        
