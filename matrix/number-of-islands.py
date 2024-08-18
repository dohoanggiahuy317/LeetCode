class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ans = 0
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        def backtrack(i, j):
            nonlocal grid, visited

            if visited[i][j] or grid[i][j] == "0":
                return

            visited[i][j] = True
            if j > 0 and grid[i][j-1] == "1":
                backtrack(i, j-1)
            if j < len(grid[0]) - 1 and grid[i][j+1] == "1":
                backtrack(i, j+1)
            if i > 0 and grid[i-1][j] == "1":
                backtrack(i-1, j)
            if i < len(grid) - 1 and grid[i+1][j] == "1":
                backtrack(i+1, j)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and visited[i][j] == False:
                    ans += 1
                backtrack(i, j)

        return ans