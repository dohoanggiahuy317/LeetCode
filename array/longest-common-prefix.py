class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        def add_node(word, first):
            nonlocal trie, all_prefix_len

            node = trie
            prefix_count, prefix_bool = 0, True

            for ch in word:
                if ch not in node:
                    node[ch] = {}
                    prefix_bool = False
                elif prefix_bool and not first:
                    prefix_count += 1
                node = node[ch]

            if not first:
                all_prefix_len = min(all_prefix_len, prefix_count)
            
        
        trie = defaultdict()
        all_prefix_len = inf
        first = True
        for s in strs:
            add_node(s, first)
            first = False

        return strs[0][:all_prefix_len]