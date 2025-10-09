class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.exist = False

class Trie:
    def __init__(self):
        self.tree = TrieNode("^")

    def insert(self, word):
        curr = self.tree
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        curr.exist = True

    def get_pref(self):
        curr = self.tree
        ans = ""
        while len(curr.children) == 1:
            char = list(curr.children.keys())[0]
            ans += char
            curr = curr.children[char]

        return ans


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        tree = Trie()

        for s in strs:
            tree.insert(s)

        return tree.get_pref()