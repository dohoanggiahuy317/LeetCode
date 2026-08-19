class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(mat), len(mat[0])

        ans = [[inf] * n for _ in range(m)]

        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    continue
                queue.append((i, j))
                ans[i][j] = 0
        visited = set(queue)

        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy

                if (nx, ny) in visited:
                    continue
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                
                if mat[nx][ny] == 0:
                    ans[nx][ny] = 0
                else:
                    ans[nx][ny] = ans[x][y] + 1

                visited.add((nx, ny))
                queue.append((nx, ny))
        
        return ans