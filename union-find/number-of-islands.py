class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def span_island(x, y):
            nonlocal m, n, DIRS, grid

            visited.add((x, y))

            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if grid[nx][ny] == "0":
                    continue
                if (nx, ny) in visited:
                    continue

                span_island(nx, ny)
                
        visited = set()
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                if (i, j) not in visited:
                    ans += 1
                    span_island(i, j)

        return ans