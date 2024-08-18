class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = []
        for i in grid:
            visited.append([0] * len(i))
        max_area = 0


        def bfs(i, j):
            nonlocal visited, grid, area
            # print(i, j)
            if (i < 0 or j < 0 or i > len(grid)-1 or j > len(grid[0])-1):
                return
             
            if visited[i][j] == 1:
                return 

            if grid[i][j] == 0:
                return

            if grid[i][j] == 1:
                visited[i][j] = 1
                area += 1

            
            bfs(i-1, j)
            bfs(i+1, j)
            bfs(i, j-1)
            bfs(i, j+1)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    area = 0
                    bfs(i, j)
                    max_area = max(area, max_area)
        # print()
        return max_area



            