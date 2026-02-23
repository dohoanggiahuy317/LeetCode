class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                count += 1 if grid[i][j] < 0 else 0

        return count
        