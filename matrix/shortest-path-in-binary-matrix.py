from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        start_x, start_y, init_dist = 0, 0, 1
        directions = [  (-1, -1), (-1, 0), (-1, 1), 
                        (0, -1), (0, 1), 
                        (1, -1), (1, 0), (1, 1)]

        if grid[start_x][start_y] == 1:
            return -1

        m, n = len(grid), len(grid[0])
        visited = [[(False, inf)] * n for _ in range(m)]
        queue = deque([(start_x, start_y, init_dist)])

        while queue:
            print(queue)
            x, y, dist = queue.popleft()
            visited[x][y] = True, min(visited[x][y][1], dist)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if ( 
                    0 <= nx < m and
                    0 <= ny < n and
                    grid[nx][ny] == 0 and 
                    not visited[nx][ny][0]
                ):
                    queue.append((nx, ny, dist + 1))
        
        if visited[-1][-1][1] != inf:
            return visited[-1][-1][1]

        return -1






        