class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(x, y, char, i):
            nonlocal m, n, grid, visited, si, sj, found

            if (x, y) in visited:
                return

            if found:
                return

            visited.add((x, y))

            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue

                if grid[nx][ny] != char:
                    continue

                if nx == si and ny == sj and i > 2:
                    found = True
                    # print(char, x, y, nx, ny)
                    return

                if (nx, ny) in visited:
                    continue

                dfs(nx, ny, char, i + 1)

            visited.remove((x, y))                

        for i in range(m):
            for j in range(n):
                char = grid[i][j]

                si, sj = i, j
                found = False
                visited = set()

                dfs(i, j, char, 0)

                if found:
                    return True

        return False