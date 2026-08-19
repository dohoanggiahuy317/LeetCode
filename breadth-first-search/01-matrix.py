class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(mat), len(mat[0])

        ans = [[-1] * n for _ in range(m)]

        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    continue
                queue.append((i, j))
                ans[i][j] = 0

        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if ans[nx][ny] != -1:
                    continue
                
                ans[nx][ny] = ans[x][y] + 1
                queue.append((nx, ny))
        
        return ans