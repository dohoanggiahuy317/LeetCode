class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y, i):
            nonlocal m, n, board, word, found, visited, DIRS

            if i == len(word) - 1:
                found = True
                return 

            visited.add((x, y))
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if (nx, ny) in visited:
                    continue
                if board[nx][ny] != word[i + 1]:
                    continue

                dfs(nx, ny, i + 1)

            visited.remove((x, y))
            



        ans = []
        for word in words:
            found = False
            visited = set()
            for i in range(m):
                if not found:
                    for j in range(n):
                        if board[i][j] == word[0]:
                            dfs(i, j, 0)
                        if found:
                            ans.append(word)
                            break
        
        return ans
