class TrieNode:
    def __init__(self, ch):
        self.ch = ch
        self.children = {}
        self.exist = False

class Trie:
    def __init__(self):
        self.root = TrieNode("^")
        self.lcp_idx = inf

    def get_prefix_by_insert(self, word):
        node = self.root
        prefix_idx, still_prefix, empty = 0, True, len(node.children) == 0


        for ch in word:
            if ch in node.children and still_prefix:
                prefix_idx += 1
            elif ch not in node.children:
                node.children[ch] = TrieNode(ch)
                still_prefix = False
                        
            node = node.children[ch]
        
        self.lcp_idx = min(self.lcp_idx if empty else len(word), prefix_idx)

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