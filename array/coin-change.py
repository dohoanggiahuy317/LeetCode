class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount + 1)
        dp[0] = 0

        for value in range(1, amount + 1):
            for coin in coins:
                prev_value = value - coin
                if prev_value >= 0:
                    dp[value] = min(dp[value], dp[prev_value] + 1)


        return dp[amount] if dp[amount] != inf else -1