class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
        def bfs(i, j):
            queue = deque([(i, j)])

            while queue:
                x, y = queue.popleft()

                for dx, dy in DIRS:
                    nx, ny = x + dx, y + dy

                    if not (0 <= nx < m and 0 <= ny < n):
                        continue
                    if grid[nx][ny] != "1":
                        continue
                    if (nx, ny) in visited:
                        continue

                    queue.append((nx, ny))
                    visited.add((nx, ny))
            
        ans = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] != "1":
                    continue
                if (i, j) in visited:
                    continue
                bfs(i, j)
                ans += 1

        return ans
