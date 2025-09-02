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

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        
        return node.exist
    
    def find_common_prefix(self):
        node = self.root
        ans = ""
        while node.children:
            if len(node.children) != 1:
                return ans

            ch, = node.children
            node, = node.children.values()
            ans += ch

        return ans
            
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        trie = Trie()
        
        for s in strs:
            if s == "":
                return ""
                
            word_prefix_len = trie.insert(s)

        return trie.find_common_prefix()