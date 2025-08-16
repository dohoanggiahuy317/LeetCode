class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.matrix_sum = [[1] * n for _ in range(m)]

        for i in range(m):
            row_sum = list(accumulate(matrix[i]))
            for j in range(n):
                a = row_sum[j - 1] if j > 0 else 0
                b = self.matrix_sum[i - 1][j] if i > 0 else 0
                self.matrix_sum[i][j] = a + b + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        t1 = self.matrix_sum[row2][col2]
        t2 = self.matrix_sum[row1 - 1][col2] if row1 > 0 else 0
        t3 = self.matrix_sum[row2][col1 - 1] if row1 > 0 else 0
        t4 = self.matrix_sum[row1 - 1][col1 - 1] if (row1 > 0 and col1 > 0) else 0

        return t4 - t3 - t2 + t1


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)