class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)

        DICT_MAP = {chr(ord("a") + i): i for i in range(26)}
        MOD = 10 ** 9 + 7

        prefix = 0
        suffix, power = 0, 1
        ans = 0

        for i in range(n - 1):
            prefix = (prefix * 26 + DICT_MAP[s[i]]) % MOD
            suffix = (DICT_MAP[s[n - 1 - i]] * power + suffix) % MOD
            power = (power * 26) % MOD

            if prefix == suffix:
                ans = i + 1

        return s[:ans]
