from typing import List
from collections import deque

DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def idx(x, y):
            return x * n + y

        def bfs(grid_1d, pos):
            nonlocal m, n

            queue = deque([(grid_1d, pos)])
            reachable = set([(grid_1d, pos)])
            land = set()

            while queue:
                # print([bin(x[0]) for x in queue])
                c_grid_1d, (c_x, c_y) = queue.popleft()

                for di, dj in DIRECTIONS:
                    n_x, n_y = c_x + di, c_y + dj
                    if not (0 <= n_x < m and 0 <= n_y < n):
                        continue
                    if (c_grid_1d, (n_x, n_y)) in reachable:
                        continue

                    bit = 1 << idx(n_x, n_y)

                    if ((c_grid_1d & bit) != 0):
                        queue.append((c_grid_1d, (n_x, n_y)))
                        reachable.add((c_grid_1d, (n_x, n_y)))
                        land.add((n_x, n_y))
                    else:
                        if ((c_grid_1d & 1) == 0):
                            n_grid_1d = (c_grid_1d | 1) | bit
                            if (n_grid_1d, (n_x, n_y)) not in reachable:
                                queue.append((n_grid_1d, (n_x, n_y)))
                                reachable.add((n_grid_1d, (n_x, n_y)))
                                land.add((n_x, n_y))

            return len(land)

        grid_1d = 0
        for i in range(m):
            for j in range(n):
                grid_1d = (grid_1d << 1) | grid[i][j]
        grid_1d <<= 1

        ans = 1
        for i in range(m):
            for j in range(n):
                if (grid_1d & (1 << idx(i, j)) == 0):
                    continue
                ans = max(ans, bfs(grid_1d, (i, j)))

        return ans