class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.exist = False

class Trie:
    def __init__(self):
        self.root = TrieNode("^")
    
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        curr.exist = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(x, y, node):
            nonlocal m, n, board, trie, path

            if board[x][y] not in node.children:
                return

            if node.children[board[x][y]].exist:
                path.append(board[x][y])
                ans.add("".join(path))
                path.pop()

            path.append(board[x][y])
            visited.add((x, y))

            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                new_node = node.children[board[x][y]]

                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if (nx, ny) in visited:
                    continue
                
                dfs(nx, ny, new_node)

            path.pop()
            visited.remove((x, y))
            return

        ans = set()
        path = []
        visited = set()
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.root)
        
        return list(ans)