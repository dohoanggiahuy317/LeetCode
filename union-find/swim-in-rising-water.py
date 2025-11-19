class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def swimmable(t):
            nonlocal n
            queue = deque([(0, 0)])
            visited = set(queue)

            while queue:
                x, y = queue.popleft()
                
                if x == n - 1 and y == n - 1:
                    return True

                for dx, dy in DIRS:
                    nx, ny = x + dx, y + dy

                    if not (0 <= nx < n and 0 <= ny < n):
                        continue 
                    
                    if (nx, ny) in visited:
                        continue

                    if grid[nx][ny] > t:
                        continue

                    queue.append((nx, ny))
                    visited.add((nx, ny))

            return False

        l, r = 0, max([max(row) for row in grid])
        best_t = -1
        while l <= r:
            m = (l + r) >> 1

            if swimmable(m):
                best_t = m
                r = m - 1
            else:
                l = m + 1

        return best_t
