class CharNode:
    def __init__(self, ch):
        self.ch = ch
        self.children = {}
        self.exist = False

class WordDictionary:

    def __init__(self):
        self.root = CharNode("^")

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = CharNode(char)
            node = node.children[char]
        node.exist = True

    def search(self, word: str) -> bool:
        queue = deque([self.root])

        for char in word:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.exist:
                    return True
                
                if char == ".":
                    for _, child in node.children.items():
                        queue.append(child)

                elif char in node.children:
                    queue.append(node.children[char])
            
        for node in queue:
            if node.exist:
                return True

        return False
                


            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)