class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        # f(i, j) = maximum profit after day i with j money left
        # f(i, j) = max(f(i-1, j), f(i, j - present[i]) + profit[i] )

        m = len(present)
        dp = [[0] * (budget + 1) for _ in range(m)]
        profit = [f - p for p, f in zip(present, future)]

        for i in range(m):
            for j in range(budget + 1):
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i - 1][j - present[i]] + profit[i] if j - present[i] >= 0 else 0
                )


        return dp[-1][-1]

