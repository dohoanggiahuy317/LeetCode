class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        DIRS = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def bfs(i, j):
            
            queue = deque([(i, j, 0)])
            visited = set([(i, j)])

            while queue:
                for _ in range(len(queue)):
                    x, y, curr_idx = queue.popleft()

                    if curr_idx == len(word) - 1:
                        return True

                    for dx, dy in DIRS:
                        nx, ny = x + dx, y + dy

                        if not (0 <= nx < m and 0 <= ny < n):
                            continue

                        if (nx, ny) in visited:
                            continue

                        next_idx = curr_idx + 1
                        if board[nx][ny] != word[next_idx]:
                            continue

                        queue.append((nx, ny, next_idx))
                        visited.add((nx, ny))

            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if bfs(i, j):
                        return True

        return False