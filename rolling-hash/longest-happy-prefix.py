class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)

        DICT_MAP = {chr(ord("a") + i): i for i in range(26)}
        prefix = 0
        suffix = 0
        ans = ""

        for i in range(n - 1):
            prefix = prefix * 26 + DICT_MAP[s[i]]
            suffix = DICT_MAP[s[n - 1 - i]] * (26 ** i) + suffix 

            if prefix == suffix:
                ans = s[:i + 1]

        return ans
