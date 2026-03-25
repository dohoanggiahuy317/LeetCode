class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        cols = [0] * n
        rows = [0] * m
        total = 0

        for i in range(m):
            for j in range(n):
                cols[j] += grid[i][j]
                rows[i] += grid[i][j]
                total += grid[i][j]

        for pref in accumulate(cols):
            if pref == total / 2:
                return True
        
        for pref in accumulate(rows):
            if pref == total / 2:
                return True

        return False