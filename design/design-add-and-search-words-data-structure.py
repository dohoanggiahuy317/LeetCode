class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.exist = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode("^")

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        
        curr.exist = True

    def search(self, word: str) -> bool:
        curr = self.root
        queue = deque([curr])

        for char in word:
            for _ in range(len(queue)):
                curr = queue.popleft()

                if char != "." and char not in curr.children:
                    continue
                elif char != ".":
                    queue.append(curr.children[char])
                else:
                    for _, neigh in curr.children.items():
                        queue.append(neigh)

        for node in queue:
            if node.exist:
                return True

        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)