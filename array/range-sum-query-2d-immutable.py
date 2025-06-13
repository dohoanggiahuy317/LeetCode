class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.temp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            pref_row = 0
            for j in range(len(matrix[0])):
                pref_row += matrix[i][j]
                self.temp[i+1][j+1] = pref_row + self.temp[i][j+1]
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rowl = min(row1, row2) + 1
        coll = min(col1, col2) + 1
        rowr = max(row1, row2) + 1
        colr = max(col1, col2) + 1
        return self.temp[rowr][colr] - self.temp[rowr][coll-1] - self.temp[rowl-1][colr] + self.temp[rowl - 1][coll - 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)