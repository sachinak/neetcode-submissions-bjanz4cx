class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = []
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        
        def dfs(x,y, idx):  
            if idx == len(word):
                return True          
            if x <0 or y<0 or x >= len(board) or y >= len(board[0]) or visited[x][y] or board[x][y] != word[idx]:
                return False
    
            visited[x][y] = True
            found = (dfs(x+1,y,idx+1)
            or dfs(x,y+1,idx+1)
            or dfs(x-1,y,idx+1)
            or dfs(x,y-1,idx+1))
            visited[x][y] = False
            return found
            
        for x in range(len(board)):
            for y in range(len(board[0])):
                if dfs(x,y,0):
                    return True
        return False
       