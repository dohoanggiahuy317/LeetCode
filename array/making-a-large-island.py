DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        comp_id = {}  
        islands = {}     
        next_id = 1

        def dfs(x, y, island_id):
            if not (0 <= x < m and 0 <= y < n):
                return 0
            if grid[x][y] != 1:
                return 0
            if (x, y) in comp_id:
                return 0

            comp_id[(x, y)] = island_id
            size = 1
            for dx, dy in DIRECTIONS:
                size += dfs(x + dx, y + dy, island_id)
            return size

        def get_island_size(i, j):
            nonlocal next_id
            islands[next_id] = dfs(i, j, next_id)
            next_id += 1

        def group_island(x, y):
            nonlocal ans
            seen = set()
            total = 1
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    island_id = comp_id[(nx, ny)]
                    if island_id not in seen:
                        seen.add(island_id)
                        total += islands[island_id]
            ans = max(ans, total)

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1 and (x, y) not in comp_id:
                    get_island_size(x, y)

        ans = max(islands.values(), default=0)
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 0:
                    group_island(x, y)

        return ans