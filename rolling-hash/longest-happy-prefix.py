class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)

        MOD = 10 ** 9 + 7
        BASE = 27
        DICT_MAP = {chr(ord("a") + i): i + 1 for i in range(BASE)}
        
        prefix = 0
        suffix, power = 0, 1
        ans = 0

        for i in range(n - 1):
            prefix = (prefix * BASE + DICT_MAP[s[i]]) % MOD
            suffix = (DICT_MAP[s[n - 1 - i]] * power + suffix) % MOD
            power = (power * BASE) % MOD

            if prefix == suffix:
                ans = i + 1

        return s[:ans]
