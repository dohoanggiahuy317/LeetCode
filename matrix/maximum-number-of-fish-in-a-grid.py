DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def start_catch(x, y):
            nonlocal grid, m, n, ans, visited, fish

            if not (0 <= x < m and 0 <= y < n):
                return
            if grid[x][y] == 0:
                return
            if (x, y) in visited:
                return

            fish += grid[x][y]
            visited.add((x, y))
            
            for i, j in DIRECTIONS:
                start_catch(x + i, y + j)

        visited = set()
        ans = 0
        for x in range(m):
            for y in range(n):
                fish = 0
                start_catch(x, y)
                ans = max(ans, fish)

        return ans

        