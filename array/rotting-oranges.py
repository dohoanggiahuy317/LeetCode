DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        good_orange = 0
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    good_orange += 1
                if grid[i][j] == 2:
                    queue.append((i, j))

        reachable = set(queue)
        time = 0

        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()

                if good_orange == 0:
                    return time

                for x, y in DIRECTIONS:
                    ni, nj = i + x, j + y

                    if not ( 0 <= ni < m and 0 <= nj < n):
                        continue
                    if grid[ni][nj] == 0:
                        continue
                    if grid[ni][nj] == 2:
                        continue

                    grid[ni][nj] = 2
                    good_orange -= 1

                    queue.append((ni, nj))
                    reachable.add((ni, nj))
            
            time += 1

        return -1



