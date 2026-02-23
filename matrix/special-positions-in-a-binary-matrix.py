class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        count = 0

        for i, row in enumerate(mat):
            if sum(row) != 1:
                continue

            j = row.index(1)

            if sum([mat[k][j] for k in range(m)]) == 1:
                count += 1

        return count