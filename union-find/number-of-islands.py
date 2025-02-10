class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        ans = 0

        def dfs(i, j):
            nonlocal grid, visited

            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return

            if grid[i][j] == "0" or visited[i][j]:
                return
            
            visited[i][j] = True

            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)

        return ans