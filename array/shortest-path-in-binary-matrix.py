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
        queue = deque([(start_x, start_y, init_dist)])
        visited = set((start_x, start_y))
        
        while queue:
            x, y, dist = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx == m - 1 and ny == n - 1 and grid[nx][ny] == 0:
                    return dist + 1

                if ( 
                    0 <= nx < m and
                    0 <= ny < n and
                    grid[nx][ny] == 0 and 
                    (nx, ny) not in visited
                ):
                    queue.append((nx, ny, dist + 1))
                    visited.add((nx, ny))
    

        return -1






        