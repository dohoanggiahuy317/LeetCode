DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def word_search(x, y, i):
            nonlocal word, found, s, m, n, visited

            if i == len(word):
                return True

            visited[x][y] = True 
                        
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                
                if visited[nx][ny]:
                    continue

                if board[nx][ny] != word[i]:
                    continue
                
                if word_search(nx, ny, i + 1):
                    return True
            
            visited[x][y] = False

            return False

        m, n = len(board), len(board[0])
        s = len(word)
        found = False
        visited = [[False] * n for _ in range(m)]

        for x in range(m):
            for y in range(n):

                if board[x][y] != word[0]:
                    continue

                if word_search(x, y, 1):
                    return True

        return False