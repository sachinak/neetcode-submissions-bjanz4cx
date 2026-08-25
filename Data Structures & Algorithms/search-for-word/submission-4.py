class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])
        visited = [[False]*cols for _ in range(rows)]

        def backtrack(i, j, idx):
            if idx == len(word):
                return True
            
            if i < 0 or j < 0 or i >= rows or j >= cols or visited[i][j] or board[i][j] != word[idx]:
                return False
            
            visited[i][j] = True
            found = (backtrack(i+1, j, idx+1) or backtrack(i-1, j, idx+1) or backtrack(i, j + 1, idx + 1) or backtrack(i, j - 1, idx + 1))
            visited[i][j] = False
            return found
        

        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        return False