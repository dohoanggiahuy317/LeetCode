class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        DIRS = [(0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)]
        n = len(grid)

        ans = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(1, n - 1):
            for j in range(1, n - 1):
                ans_i, ans_j = i - 1, j - 1

                val = max(grid[i + di][j + dj] for di, dj in DIRS)
                ans[ans_i][ans_j] = val


        return ans