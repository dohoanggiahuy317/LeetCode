class TrieNode:
    def __init__(self, ch):
        self.ch = ch
        self.children = {}
        self.exist = False

class Trie:
    def __init__(self):
        self.tree = TrieNode("^")

    def insert(self, word):
        node = self.tree
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.exist = True
    
    def suggest(self, word):
        node = self.tree
        for char in word:
            if char not in node.children:
                return []
            node = node.children[char]
        
        queue = [(node.ch, node, word) for node in list(node.children.values())]
        ans = [word] if node.exist else []
        while queue:
            curr_char, curr_node, curr_word = heapq.heappop(queue)

            next_word = curr_word + curr_char
            if curr_node.exist:
                ans.append(next_word)

            for next_char, next_node in curr_node.children.items():
                heapq.heappush(queue, (next_char, next_node, next_word))

        return sorted(ans)[:3]


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)
        
        ans = []
        for i in range(1, len(searchWord) + 1):
            ans.append(trie.suggest(searchWord[:i]))

        return ans