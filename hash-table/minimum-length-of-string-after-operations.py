from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        d = Counter()

        for ch in list(s):
            d[ch] += 1

        ans = 0

        for u, v in d.items():
            if v == 1 or v == 2:
                ans += v
            elif v % 2 == 0:
                ans += 2
            else:
                ans += 1
        return ans