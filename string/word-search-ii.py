DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class TrieNode:
    def __init__(self, ch):
        self.ch = ch
        self.children = {}
        self.exist = False

class Trie:
    def __init__(self):
        self.root = TrieNode("^")

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode(ch)
            node = node.children[ch]
        node.exist = True
            

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(x, y, node, step):
            nonlocal visited, curr_word, ans, m, n

            
            visited[x][y] = True
            ch = board[x][y]
            curr_word.append(ch)

            if node.exist:
                ans.add("".join(curr_word))
            
            if step == 10:
                return

            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue

                next_ch = board[nx][ny]
                if next_ch not in node.children:
                    continue

                dfs(nx, ny, node.children[next_ch], step + 1)
  

            visited[x][y] = False
            curr_word.pop()

        m, n = len(board), len(board[0])
        ans = set()
        curr_word = []
        visited = [[False] * n for _ in range(m)]
        
        for x in range(m):
            for y in range(n):
                if board[x][y] in trie.root.children:
                    char = board[x][y]
                    dfs(x, y, trie.root.children[char], 0)

        return list(ans)



