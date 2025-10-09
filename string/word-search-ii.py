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
        trie = Trie()
        for word in words:
            trie.insert(word)

        m, n = len(board), len(board[0])
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y, curr_word, node):
            if board[x][y] not in node.children:
                return
            
            char = board[x][y]            
            visited[(x, y)] = True
            curr_word.append(char)
            next_node = node.children[char]
            if next_node.exist:
                ans.add("".join(curr_word))

            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if visited[(nx, ny)]:
                    continue
                dfs(nx, ny, curr_word, next_node)
            
            visited[(x, y)] = False
            curr_word.pop()

        ans = set()
        for i in range(m):
            for j in range(n):
                visited = defaultdict(bool)
                dfs(i, j, [], trie.root)

        return list(ans)
            

            
