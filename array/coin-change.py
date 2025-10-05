class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(amount + 1):
                if amount + 1 > i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[-1] if dp[-1] != inf else -1

