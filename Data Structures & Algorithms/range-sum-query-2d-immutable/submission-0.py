class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.mat = []
        for i in range(rows+1):
            row = []
            for j in range(cols+1):
                row.append(0)
            self.mat.append(row)
        
        for i in range(rows):
            row = 0
            for j in range(cols):
                row += matrix[i][j]
                above = self.mat[i][j+1]
                self.mat[i+1][j+1] = row + above
        


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,row2,col1,col2 = row1+1,row2+1,col1+1,col2+1
        a = self.mat[row2][col2]
        b = self.mat[row1 - 1][col2]
        c = self.mat[row2][col1 - 1]
        d = self.mat[row1-1][col1-1]
        return a - b - c + d


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)