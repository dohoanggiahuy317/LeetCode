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
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.exist = True

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)
        self.queue = deque()
        

    def query(self, letter: str) -> bool:
        self.queue.append(self.trie.root)
        exist = False

        for _ in range(len(self.queue)):
            node = self.queue.popleft()

            if letter in node.children:
                child = node.children[letter]
                self.queue.append(node.children[letter])

                exist = exist or child.exist

        return exist


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)