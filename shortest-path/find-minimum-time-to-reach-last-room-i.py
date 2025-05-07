class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        dp = [[-float("INF")] * len(moveTime[0]) for _ in range(len(moveTime))]

        dp[0][0] = 0

        for i in range(1, len(moveTime)):
            dp[i][0] = max(dp[i-1][0] + 1, moveTime[i][0] + 1)
        for j in range(1, len(moveTime[0])):
            dp[0][j] = max(dp[0][j-1] + 1, moveTime[0][j] + 1)

        for i in range(1, len(moveTime)):
            for j in range(1, len(moveTime[0])):
                dp[i][j] = max( moveTime[i][j] + 1, min(dp[i][j-1] + 1, dp[i-1][j] + 1) )

        return dp[-1][-1]