class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y, i):
            nonlocal word, board, m, n, DIRS, visited, found

            if i == len(word) - 1:
                found = True
                return

            visited.add((x, y))

            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if board[nx][ny] != word[i + 1]:
                    continue
                if (nx, ny) in visited:
                    continue

                dfs(nx, ny, i + 1)

            visited.remove((x, y))


        found = False
        for i in range(m):
            for j in range(n):
                visited = set()
                if board[i][j] == word[0]:
                    dfs(i, j, 0)

                if found:
                    return True

        return False
    