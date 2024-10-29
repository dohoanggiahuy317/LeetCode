class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])


        dp = [[0] * n for _ in range(m)]


        for j in range(n-2, -1, -1):
            for i in range(m-1, -1, -1):
            
                temp = 0
                if i > 0 and grid[i][j] < grid[i-1][j+1]:
                    temp = max(temp, dp[i-1][j+1]+1)
                
                if i < m-1 and grid[i][j] < grid[i+1][j+1]:
                    temp = max(temp, dp[i+1][j+1]+1)
                
                if grid[i][j] < grid[i][j+1]:
                    temp = max(temp, dp[i][j+1]+1)

                dp[i][j] = temp


        return max(list(map(lambda x: x[0], dp)))

        



        # def backtrack(i, j, curr):
        #     nonlocal m, n, temp

        #     temp = max(temp, curr)

        #     if j >= n-1:
        #         return
            
        #     if j<n-1 and i>0 and grid[i][j] < grid[i-1][j+1]:
        #         backtrack(i-1, j+1, curr+1)
        #     if j<n-1 and grid[i][j] < grid[i][j+1]:
        #         backtrack(i, j+1, curr+1)
        #     if j<n-1 and i<m-1 and grid[i][j] < grid[i+1][j+1]:
        #         backtrack(i+1, j+1, curr+1)


        # ans = 0
        # for i in range(m):
        #     temp = 0
        #     backtrack(i, 0, 0)
        #     ans = max(ans, temp)

        # return ans



