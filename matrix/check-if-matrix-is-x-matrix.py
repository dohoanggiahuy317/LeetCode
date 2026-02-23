class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            if grid[i][i] == 0 or grid[n - 1 - i][i] == 0:
                return False

            for j in range(n):
                if j == i or j == n - 1 - i:
                    continue
                if grid[i][j] != 0:
                    return False

        return True