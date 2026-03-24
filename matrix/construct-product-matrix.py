class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        prefix = []
        suffix = []

        for i in range(m):
            for j in range(n):
                pref_cell = 1 if not prefix else prefix[-1]
                prefix.append((grid[i][j] * pref_cell) % 12345)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                suff_cell = 1 if not suffix else suffix[-1]
                suffix.append((grid[i][j] * suff_cell) % 12345)

        suffix.reverse()
        p = [[1] * n for _ in range(m)]
        counter = 0

        for i in range(m):
            for j in range(n):
                pref = prefix[counter - 1] if counter > 0 else 1
                suff = suffix[counter + 1] if counter < m * n - 1 else 1
                p[i][j] = (pref * suff) % 12345
                counter += 1

        return p