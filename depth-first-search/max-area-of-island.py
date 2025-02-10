class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        ans = 0

        def dfs(i, j):
            nonlocal grid, visited
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
            
            if visited[i][j] or grid[i][j] == 0:
                return 0

            visited[i][j] = True

            return 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j+1) + dfs(i, j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))

        return ans
