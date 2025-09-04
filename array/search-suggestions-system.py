class TrieNode:
    def __init__(self, ch):
        self.ch = ch
        self.children = {}
        self.best3 = []
        self.exist = False

class Trie:
    def __init__(self):
        self.root = TrieNode("^")
    
    def add_node(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode(ch)
                node.best3 = sorted(node.best3 + [ch])[:3]
            node = node.children[ch]
        
        node.exist = True

    def find_word(self, word):
        
        # Find the node that contain the word
        node = self.root
        for ch in word:
            if ch not in node.children:
                return []
            node = node.children[ch]
        
        # find the node that exist starting from node
        queue = deque([("", node)])
        words = []

        while queue and len(words) < 3:
            subword, node = queue.pop(0)
            
            if node.exist:
                words.append(word + subword)
            
            for child_char, child_node in node.children.items():
                queue.append((subword + child_char, child_node))
                queue.sort()
                if len(queue) > 3:
                    queue.pop()

        return words

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        trie = Trie()

        for prod in products:
            trie.add_node(prod)

        ans = []
        for i in range(1, len(searchWord) + 1):
            t = trie.find_word(searchWord[:i])
            ans.append(t)
        
        return ans
