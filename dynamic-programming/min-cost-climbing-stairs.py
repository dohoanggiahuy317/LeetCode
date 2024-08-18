class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = { -1: 0, 0: cost[0]}

        for i in range(1, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])


        return min(dp[len(cost) - 1], dp[len(cost) - 2])
        