class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])

        queue = deque()
        visited = set()
        for x in range(m):
            for y in range(n):
                if grid[x][y] != 1:
                    continue
                queue.append((x, y, 0))
                visited.add((x, y))
        
        far = -1

        while queue:
            x, y, d = queue.popleft()

            for dx, dy in DIRS:
                nx, ny, nd = x + dx, y + dy, d + 1
                
                if (nx, ny) in visited:
                    continue
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                
                far = max(far, nd)
                queue.append((nx, ny, nd))
                visited.add((nx, ny))

        return far

