class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter()

        for c in s:
            d[c] += 1

        odd = 0
        ans = 0

        for u, v in d.items():
            if v % 2 == 0:
                ans += v
            else:
                odd = 1
                ans += v - 1

        return ans + (odd+1)//2
        