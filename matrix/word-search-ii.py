DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class TrieNode:
    def __init__(self, ch):
        self.ch = ch
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode("^")

    def insert_board(self, board):
        m, n = len(board), len(board[0])
        
        for x in range(m):
            for y in range(n):
                visited = [[False] * n for _ in range(m)]
                self.dfs_word(board, visited, self.root, x, y)

    def dfs_word(self, board, visited, node, x, y):
        
        m, n = len(board), len(board[0])

        ch = board[x][y]

        if ch not in node.children:
            node.children[ch] = TrieNode(ch)
            
        visited[x][y] = True

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < m and 0 <= ny < n):
                continue

            if visited[nx][ny]:
                continue

            self.dfs_word(board, visited, node.children[ch], nx, ny)
        
        visited[x][y] = False


    def search(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                return False

            node = node.children[ch]

        return True
            

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        trie.insert_board(board)

        ans = []

        for word in words:
            if trie.search(word):
                ans.append(word)

        return ans



