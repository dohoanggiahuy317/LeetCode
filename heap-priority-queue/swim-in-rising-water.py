DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Constant
        m, n = len(grid), len(grid[0])
        S_X, S_Y = 0, 0
        T_X, T_Y = m - 1, n - 1
        SWIMABLE, UNSWIMABLE = True, False
        
        # can_swim
        def can_swim(target_time):
            nonlocal S_X, S_Y, T_X, T_Y

            queue = deque([ (S_X, S_Y) ])
            reachable = set(queue)

            while queue:
                for _ in range(len(queue)):
                    cx, cy = queue.popleft()

                    if cx == T_X and cy == T_Y:
                        return SWIMABLE

                    for i, j in DIRECTIONS:
                        nx, ny = cx + i, cy + j

                        if not(0 <= nx < m and 0 <= ny < n):
                            continue
                        
                        if grid[nx][ny] > target_time:
                            continue
                        
                        if (nx, ny) in reachable:
                            continue

                        queue.append( (nx, ny) )
                        reachable.add((nx, ny))

            return UNSWIMABLE

        # START SWIMING
        l = grid[S_X][S_Y]
        r = max(max(row) for row in grid)
        ans = -1
        
        while l <= r:
            m_target_time = (l + r) // 2

            if can_swim(m_target_time):
                ans = m_target_time
                r = m_target_time - 1
            else:
                l = m_target_time + 1

        return ans
