class TrieNode:
    def __init__(self, ch):
        self.ch = ch
        self.children = {}
        self.exist = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode("^")

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode(ch)
            node = node.children[ch]

        node.exist = True

    def search(self, word: str) -> bool:
        queue = deque([self.root])

        for ch in word:
            for _ in range(len(queue)):
                node = queue.popleft()

                if ch.isalpha() and ch in node.children:
                    queue.append(node.children[ch])

                elif ch == ".":
                    for child in node.children.values():
                        queue.append(child)

        for node in queue:
            if node.exist:
                return True

        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)