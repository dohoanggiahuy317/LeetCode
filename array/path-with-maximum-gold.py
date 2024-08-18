class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        

        def dfs(i, j):
            nonlocal grid, m, n, visited, money, curr_max
            if (i < 0 or i >= m) or (j < 0 or j >= n):
                return
            if grid[i][j] == 0 or visited[i][j]:
                return
        
            visited[i][j] = True
            money += grid[i][j]
            curr_max = max(money, curr_max)
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
            money -= grid[i][j]
            visited[i][j] = False

            return


        m, n = len(grid), len(grid[0])
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    visited = [[False] * n for _ in range(m)]
                    money, curr_max = 0, 0
                    dfs(i, j)
                    ans = max(ans, curr_max)


        return ans



                    