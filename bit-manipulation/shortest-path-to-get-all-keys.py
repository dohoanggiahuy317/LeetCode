class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        KEY_DICT = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
        }
        
        def bfs(i, j):
            nonlocal m, n

            q = deque([(i, j, 0)])
            visited = set(q)
            step = 0

            while q:
                for _ in range(len(q)):
                    x, y, cur_k = q.popleft()

                    if cur_k == (1 << k) - 1:
                        return step

                    for dx, dy in DIRECTIONS:
                        nx, ny = x + dx, y + dy

                        if not (0 <= nx < m and 0 <= ny < n):
                            continue
                        if grid[nx][ny] == "#":
                            continue
                        
                        if grid[nx][ny].isalpha() and grid[nx][ny].isupper():
                            if not (cur_k >> KEY_DICT[grid[nx][ny].lower()] & 1):
                                continue
                        
                        new_k = cur_k
                        if grid[nx][ny].isalpha() and grid[nx][ny].islower():
                            new_k = cur_k | (1 << KEY_DICT[grid[nx][ny]])
                        if (nx, ny, new_k) in visited:
                            continue

                        q.append((nx, ny, new_k))
                        visited.add((nx, ny, new_k))

                step += 1

            return -1

        s_x, s_y = (0, 0)
        k = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j].isalpha() and grid[i][j].islower():
                   k += 1
                elif grid[i][j] == "@":
                    s_x, s_y = i, j

        return bfs(s_x, s_y)