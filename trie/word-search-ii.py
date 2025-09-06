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
        
        # INSERT TRIE
        trie = Trie()
        for word in words:
            trie.insert(word)

        # DFS FOR EACH WORD
        def dfs(x, y, node, step):
            nonlocal visited, curr_word, ans, m, n
        
            # no word has length > 10
            if step == 10:
                return
            
            # if cannot make word from this path
            ch = board[x][y]
            if ch not in node.children:
                return

            # get the word
            visited[x][y] = True
            curr_word.append(ch)
            next_node = node.children[ch]

            if next_node.exist: # Found word here
                ans.add("".join(curr_word))

            # explore other
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if visited[nx][ny]:
                    continue
                
                dfs(nx, ny, next_node, step + 1)
  

            visited[x][y] = False
            curr_word.pop()

        m, n = len(board), len(board[0])
        ans = set()
        curr_word = []
        visited = [[False] * n for _ in range(m)]
        
        for x in range(m):
            for y in range(n):
                dfs(x, y, trie.root, 0)

        return list(ans)



