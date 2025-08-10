DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Constant
        m, n = len(grid), len(grid[0])
        S_X, S_Y = 0, 0
        T_X, T_Y = m - 1, n - 1
        SWIMABLE, UNSWIMABLE = True, False
        
        # BFS
        def bfs(target_time):
            nonlocal S_X, S_Y, T_X, T_Y

            queue = deque([ (S_X, S_Y) ])
            reachable = set(queue)

            while queue:
                for _ in range(len(queue)):
                    c_x, c_y = queue.popleft()

                    if c_x == T_X and c_y == T_Y:
                        return SWIMABLE

                    for i, j in DIRECTIONS:
                        n_x, n_y = c_x + i, c_y + j

                        if not(0 <= n_x < m and 0 <= n_y < n):
                            continue
                        
                        if grid[n_x][n_y] > target_time:
                            continue
                        
                        if (n_x, n_y) in reachable:
                            continue

                        queue.append( (n_x, n_y) )
                        reachable.add((n_x, n_y))

            return UNSWIMABLE

        # START SWIMING
        l, r = inf, -inf
        for row in grid:
            for cell in row:
                l = min(cell, l)
                r = max(cell, r)
        ans = -1
        
        while l <= r:
            m_target_time = (l + r) // 2

            if bfs(m_target_time):
                ans = m_target_time
                r = m_target_time - 1
            else:
                l = m_target_time + 1

        return ans
