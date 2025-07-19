class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.ps = [[0] * n for _ in range(m)]

        for i in range(m):
            prefSum = [0] * n
            prefSum[0] = matrix[i][0]
            for j in range(n):
                prefSum[j] = (prefSum[j - 1] if j > 0 else 0) + matrix[i][j]
                square_sum = prefSum[j]
                if i > 0:
                    square_sum += self.ps[i - 1][j]
                self.ps[i][j] = square_sum

                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left_square = self.ps[row2][col1 - 1] if col1 > 0 else 0
        upper_square = self.ps[row1 - 1][col2] if row1 > 0 else 0
        diag_square = self.ps[row1 - 1][col1 - 1] if (row1 > 0 and col1 > 0) else 0
        return self.ps[row2][col2] - left_square - upper_square + diag_square


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)