START_X, START_Y = 0, 0
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        START_TIME = grid[START_X][START_Y]
        queue = deque([ (START_X, START_Y, START_TIME) ])
        reachable = defaultdict(lambda : inf)
        ans = inf

        while queue:
            for _ in range(len(queue)):
                cur_x, cur_y, cur_time = queue.popleft()

                if cur_x == m - 1 and cur_y == n - 1:
                    ans = min(ans, cur_time)

                for i, j in DIRECTIONS:
                    n_x, n_y, n_time = cur_x + i, cur_y + j, cur_time

                    if not(0 <= n_x < m and 0 <= n_y < n):
                        continue
                    
                    if grid[n_x][n_y] > cur_time:
                        n_time = grid[n_x][n_y]

                    if reachable[(n_x, n_y)] <= n_time:
                        continue

                    queue.append( (n_x, n_y, n_time) )
                    reachable[(n_x, n_y)] = n_time

        return ans