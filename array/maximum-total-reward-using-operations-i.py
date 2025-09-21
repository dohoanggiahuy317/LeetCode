class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        
        n = len(rewardValues)
        rewardValues.sort()
        dp = [rewardValues[0]] * n

        for i, reward in enumerate(rewardValues):
            local_max = 0

            for j in range(i):
                if reward > dp[j]:
                    local_max = max(local_max, dp[j] + reward)

            dp[i] = max(local_max, dp[i])

        return dp[-1]



        