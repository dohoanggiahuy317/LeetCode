DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def word_search(x, y, visited, curr_word):
            nonlocal word, found, s, m, n

            if len(curr_word) == s:
                found = curr_word == word
                return
                        
            for i, j in DIRECTIONS:
                if found:
                    return

                if not (0 <= x + i < m and 0 <= y + j < n):
                    continue
                
                if visited[x + i][y + j]:
                    continue
                
                visited[x + i][y + j] = True  
                word_search(x + i, y + j, visited, curr_word + board[x + i][y + j])
                visited[x + i][y + j] = False

        m, n = len(board), len(board[0])
        s = len(word)
        found = False

        for x in range(m):
            for y in range(n):
                visited = [[False] * n for _ in range(m)]
                visited[x][y] = True
                word_search(x, y, visited, board[x][y])

                if found:
                    return True

        return False