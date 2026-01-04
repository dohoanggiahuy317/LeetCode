MOD = 10**9 + 7

class Solution:
    def countPalindromes(self, s: str) -> int:
        n = len(s)
        if n < 5:
            return 0

        def count_subseq(sub_s):
            # dp[js
            dp = [0] * 6
            dp[0] = 1
            for ch in s:
                for j in range(4, -1, -1):
                    if ch == sub_s[j]:
                        dp[j + 1] = (dp[j + 1] + dp[j]) % MOD
            return dp[5]

        ans = 0
        for a in '0123456789':
            for b in '0123456789':
                for c in '0123456789':
                    t = a + b + c + b + a
                    ans = (ans + count_subseq(t)) % MOD

        return ans