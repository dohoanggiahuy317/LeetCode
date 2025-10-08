class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def bfs(src):
            nonlocal keys_set, m, n

            q = deque([src])
            visited = set(q)
            step = 0

            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()

                    if (x, y) in keys_set:
                        keys_set.remove((x, y))
                        key_found[grid[x][y].upper()] = True
                        return (x, y), step

                    for dx, dy in DIRECTIONS:
                        nx, ny = x + dx, y + dy

                        if not (0 <= nx < m and 0 <= ny < n):
                            continue
                        if grid[nx][ny] == "#":
                            continue
                        if grid[nx][ny].isalpha() and grid[nx][ny].isupper():
                            if not key_found[grid[nx][ny]]:
                                continue

                        q.append((nx, ny))
                        visited.add((nx, ny))

                step += 1

            return (-1, -1), -1

        keys_set = set()
        key_found = {}
        curr_start = (0, 0)
        for i in range(m):
            for j in range(n):
                if grid[i][j].isalpha() and grid[i][j].islower():
                    keys_set.add((i, j))
                elif grid[i][j].isalpha() and grid[i][j].isupper():
                    key_found[grid[i][j]] = False
                elif grid[i][j] == "@":
                    curr_start = (i, j)

        ans = 0
        while keys_set:
            curr_start, step = bfs(curr_start)
            ans += step
            if curr_start == (-1, -1):
                return -1

        return ans