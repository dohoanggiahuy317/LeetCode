class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)
        count = 0

        def dfs(prev_sum, i):
            nonlocal n, amount, count, dp
            if prev_sum > amount:
                return 0
            if prev_sum == amount:
                return 1
            if i > n-1:
                return 0
            if dp[prev_sum][i] != -1:
                return dp[prev_sum][i]

            dp[prev_sum][i] = dfs(prev_sum + coins[i], i) + dfs(prev_sum, i + 1)
            return dfs(prev_sum, i)

        dp = [ [-1] * n for _ in range(amount + 1) ]

        return dfs(0, 0)