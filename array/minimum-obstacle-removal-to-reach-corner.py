class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        cost = [[inf] * n for _ in range(m)]
        cost[0][0] = 0

        queue = [(0, 0)]
        ans = inf

        while queue:
            x, y = heapq.heappop(queue)

            if (x, y) == (m - 1, n - 1):
                ans = min(ans, cost[x][y])
                return ans

            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                new_cost = cost[x][y]
                
                if grid[nx][ny] == 1:
                    new_cost = cost[x][y] + 1
                
                if new_cost < cost[nx][ny]:
                    cost[nx][ny] = new_cost
                    heapq.heappush(queue, (nx, ny))

        return ans
            