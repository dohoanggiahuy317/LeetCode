class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n * k < target:
            return 0

        MOD = 10**9 + 7
        
        dp = []
        for i in range(n+1):
            temp_dp = [0] * (target+1)
            dp.append(temp_dp)
        dp[0][0] = 1

        for dice in range(1, n+1):
            for achieve in range(dice, min(dice*k, target) + 1):
                for prev_achieve in range(1, min(k, achieve) + 1):
                    dp[dice][achieve] = (dp[dice][achieve] + dp[dice-1][achieve - prev_achieve]) % MOD

        return dp[n][target]

