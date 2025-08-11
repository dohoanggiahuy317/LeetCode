DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            nonlocal size, visited, grid, m, n
            if not (0 <= x < m and 0 <= y < n):
                return
            if grid[x][y] == 0:
                return
            if (x, y) in visited:
                return
            
            visited.add((x, y))
            size += 1
            for i, j in DIRECTIONS:
                dfs(x + i, y + j)

        def get_island_size(i, j):
            nonlocal visited, size, grid, islands

            for island in islands:
                if (i, j) in island:
                    return

            dfs(i, j)    
            islands[tuple(visited)] = size

        def group_island(x, y):
            nonlocal grid, ans

            found_island = set()
            group_island_size = 0

            for i, j in DIRECTIONS:
                nx, ny = x + i, y + j

                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if grid[nx][ny] == 1 and (nx, ny) not in found_island:
                    for island, size in islands.items():
                        if (nx, ny) in island:
                            found_island.update(island)
                            group_island_size += size
            ans = max(ans, group_island_size + 1)
            return

        islands = {}
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    visited, size  = set(), 0
                    get_island_size(x, y)
                        
        # print(islands)
        
        ans = max(islands.values()) if islands else 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 0:
                    group_island(x, y)

        return ans