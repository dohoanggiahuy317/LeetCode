class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        char_ord = [ord(c) - 97 for c in s]

        def find_dup(length):

            h = 0
            for i in range(length):
                h = h * 26 + char_ord[i]

            seen = {h}
            for i in range(length, n):
                h = h - (char_ord[i - length] * (26 ** (length - 1)))
                h = h * 26 + char_ord[i]

                if h in seen:
                    return i - length + 1
                seen.add(h)
            # print(seen)
            return -1

        l, r = 1, n - 1
        ans_idx = -1
        ans_len = 0
        while l <= r:
            m = (l + r) // 2
            idx = find_dup(m)
            
            if idx != -1:              
                ans_idx = idx
                ans_len = m
                l = m + 1 
            else:
                r = m - 1

        return s[ans_idx:ans_idx + ans_len] if ans_idx != -1 else ""