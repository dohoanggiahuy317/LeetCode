class TrieNode:
    def __init__(self, ch):
        self.ch = ch
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

    def get_common_prefix(self):
        curr = self.root
        ans = ""

        while curr and len(curr.children) == 1:
            char = list(curr.children.keys())[0]
            ans += char
            curr = curr.children[char]

        return ans

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()

        for word in strs:
            trie.insert(word)

        return trie.get_common_prefix()