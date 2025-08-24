DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def start_catch(x, y):
            nonlocal grid, m, n, visited

            if not (0 <= x < m and 0 <= y < n):
                return 0
            if (x, y) in visited:
                return 0
            if grid[x][y] == 0:
                return 0
            
            visited.add((x, y))
            fish = grid[x][y]

            for i, j in DIRECTIONS:
                fish += start_catch(x + i, y + j)
            
            return fish

        visited = set()
        ans = 0
        for x in range(m):
            for y in range(n):
                fish = start_catch(x, y)
                ans = max(ans, fish)

        return ans

        