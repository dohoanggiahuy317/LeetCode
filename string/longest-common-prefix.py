class TrieNode:
    def __init__(self, ch):
        self.ch = ch
        self.children = {}
        self.exist = False

class Trie:
    def __init__(self):
        self.root = TrieNode("^")
        self.empty = True
        self.lcp_idx = inf

    def get_prefix_by_insert(self, word):
        node = self.root
        prefix_idx = 0

        for ch in word:
            if ch not in node.children:
                if self.empty:
                    node.children[ch] = TrieNode(ch)
                    self.lcp_idx = prefix_idx
                else:
                    self.lcp_idx = min(self.lcp_idx, prefix_idx)
                    return
            
            prefix_idx += 1
            node = node.children[ch]
        
        self.empty = False

    def get_lcp(self):
        node = self.root

        lcp = ""
        lcp_idx = 0 if self.lcp_idx == inf else self.lcp_idx
        for _ in range(lcp_idx):
            ch, = node.children
            lcp += ch

            node, = node.children.values()

        return lcp        
            
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        trie = Trie()
        
        for s in strs:
            word_prefix_len = trie.get_prefix_by_insert(s)
        
        return trie.get_lcp()