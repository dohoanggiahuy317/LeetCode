class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = [[inf] * n for _ in range(m)]

        sx, sy = 0, 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    sx, sy = i, j
                    ans[i][j] = 0
                    break
        
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        queue = deque([(sx, sy)])
        visited = set(queue)

        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy

                if (nx, ny) in visited:
                    continue
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                
                if mat[nx][ny] == 0:
                    ans[nx][ny] = 0
                else:
                    ans[nx][ny] = ans[x][y] + 1

                visited.add((nx, ny))
                queue.append((nx, ny))
        
        return ans