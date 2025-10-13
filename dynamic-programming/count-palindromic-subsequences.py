MOD = 10**9 + 7

class Solution:
    def countPalindromes(self, s: str) -> int:
        n = len(s)
        if n < 5:
            return 0

        def count_subseq(S, T):
            n, m = len(S), len(T)
            dp = [[0]*m for _ in range(n)]

            dp[0][0] = 1 if S[0] == T[0] else 0
            for i in range(1, n):
                dp[i][0] = dp[i-1][0] + (1 if S[i] == T[0] else 0)

            for i in range(1, n):
                for j in range(1, m):
                    dp[i][j] = dp[i-1][j]
                    if S[i] == T[j]:
                        dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % MOD

            return dp[n-1][m-1]

        ans = 0
        for a in '0123456789':
            for b in '0123456789':
                for c in '0123456789':
                    t = a + b + c + b + a
                    ans = (ans + count_subseq(s, t)) % MOD

        return ans