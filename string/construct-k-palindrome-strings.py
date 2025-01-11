class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        d = Counter()

        for i in range(len(s)):
            d[s[i]] += 1

        ans = 0
        for u, v in d.items():
            if v % 2 == 1:
                ans += 1

        if len(d) < k:
            return False

        return True if ans <= k else False