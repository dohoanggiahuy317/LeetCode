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
                else:
                    self.lcp_idx = self.lcp_idx if prefix_idx > self.lcp_idx else prefix_idx
                    return
            
            prefix_idx += 1
            node = node.children[ch]
        
        self.empty = False
        
            
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        trie = Trie()
        
        for s in strs:
            word_prefix_len = trie.get_prefix_by_insert(s)
        
        foo_str = strs[0]
        return foo_str[:trie.lcp_idx]