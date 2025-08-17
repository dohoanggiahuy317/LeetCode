DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # CONSTANT
        m, n = len(grid), len(grid[0])
        START_X, START_Y = 0, 0
        EMPTY, OBSTACBLE = 0, 1

        # BFS
        queue = deque([(START_X, START_Y, k)])
        reachable = set(queue)
        step = 0

        while queue:
            for _ in range(len(queue)):
                curr_x, curr_y, curr_k = queue.popleft()

                # reach destination
                if (curr_x, curr_y) == (m - 1, n - 1):
                    return step

                for i, j in DIRECTIONS:
                    n_x, n_y, n_k = curr_x + i, curr_y + j, curr_k

                    if not (0 <= n_x < m and 0 <= n_y < n):
                        continue

                    if grid[n_x][n_y] == OBSTACBLE:
                        if curr_k == 0:
                            continue
                        n_k -= 1

                    if (n_x, n_y, n_k) in reachable:
                        continue
                    
                    queue.append((n_x, n_y, n_k))
                    reachable.add((n_x, n_y, n_k))

            step += 1

        return -1