class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        cost = [[inf] * n for _ in range(m)]
        cost[0][0] = 0

        queue = [(0, 0, 0)]

        while queue:
            curr_cost, x, y = heapq.heappop(queue)

            if (x, y) == (m - 1, n - 1):
                return curr_cost

            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                new_cost = curr_cost
                
                if grid[nx][ny] == 1:
                    new_cost = curr_cost + 1
                
                if new_cost < cost[nx][ny]:
                    cost[nx][ny] = new_cost
                    heapq.heappush(queue, (new_cost, nx, ny))

        return -1
            