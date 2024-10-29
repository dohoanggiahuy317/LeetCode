class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def backtrack(i, j, curr):
            nonlocal m, n, temp

            temp = max(temp, curr)

            if j >= n-1:
                return
            
            if j<n-1 and i>0 and grid[i][j] < grid[i-1][j+1]:
                backtrack(i-1, j+1, curr+1)
            if j<n-1 and grid[i][j] < grid[i][j+1]:
                backtrack(i, j+1, curr+1)
            if j<n-1 and i<m-1 and grid[i][j] < grid[i+1][j+1]:
                backtrack(i+1, j+1, curr+1)


        ans = 0
        for i in range(m):
            temp = 0
            backtrack(i, 0, 0)
            ans = max(ans, temp)

        return ans



        # dp = [[0] * (n+1) for _ in range(m + 1)]

        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         temp = 0

        #         if j < n-1 and i > 0 and grid[i][j] < grid[i-1][j+1]:
        #             temp = max(temp, dp grid[i-1][j+1])

        