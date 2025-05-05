class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = {
            1: 1, 
            2: 2, 
            3: 5, 
            4: 11,
            5: 24}

        def find(n):
            nonlocal dp

            if n in dp:
                return dp[n]

            dp[n] = (2*find(n-1) % MOD + find(n-3)% MOD)% MOD
            return dp[n]% MOD

        find(n)
        return dp[n]% MOD
        