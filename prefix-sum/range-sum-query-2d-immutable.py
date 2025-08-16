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
        rmax, rmin = max(row1, row2), min(row1, row2)
        cmax, cmin = max(col1, col2), min(col1, col2)

        t1 = self.matrix_sum[rmax][cmax]
        t2 = self.matrix_sum[rmin - 1][cmax] if rmin > 0 else 0
        t3 = self.matrix_sum[rmax][cmin - 1] if cmin > 0 else 0
        t4 = self.matrix_sum[rmin - 1][cmin - 1] if (rmin > 0 and cmin > 0) else 0

        return t4 - t3 - t2 + t1


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)