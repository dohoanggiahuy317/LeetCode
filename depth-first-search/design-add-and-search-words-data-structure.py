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

        def dfs(node, i):
            nonlocal word

            if i == len(word):
                if node.exist:
                    return True
                return False

            ch = word[i]

            if ch.isalpha() and ch in node.children:
                return dfs(node.children[ch], i + 1)
            elif ch == ".":
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True

            return False

        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)