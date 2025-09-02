class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        def add_node(word):
            nonlocal trie, all_prefix_len

            node = trie
            word_prefix_len, still_prefix, first_word = 0, True, len(node) == 0

            for ch in word:
                if ch in node and still_prefix:
                    word_prefix_len += 1
                elif ch not in node:
                    node[ch] = {}
                    still_prefix = False
                    
                node = node[ch]

            # only calculate prefix length if first word is added
            return word_prefix_len if not first_word else len(word)  
        
        trie = defaultdict()
        all_prefix_len = inf
        for s in strs:
            word_prefix_len = add_node(s)
            all_prefix_len = min(all_prefix_len, word_prefix_len)

        return strs[0][:word_prefix_len]