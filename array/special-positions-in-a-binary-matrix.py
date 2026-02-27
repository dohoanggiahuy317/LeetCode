class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        row_sum = [0] * m
        col_sum = [0] * n

        # count the number of 1 for each row and column
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_sum[i] += 1
                    col_sum[j] += 1

        # only consider pair of i, j where the sum of both
        # column and row is 1, and the value itself is 1
        count = 0
        for i in range(m):
            if row_sum[i] != 1:
                continue
            for j in range(n):
                if mat[i][j] == 1 and col_sum[j] == 1:
                    count += 1

        return count