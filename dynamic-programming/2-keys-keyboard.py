import math

class Solution:
    def minSteps(self, n: int) -> int:

        dp = {
            1: 0, 
            2: 2,
            3: 3}

        for i in range(3, n+1):
            dp[i] = i
            for j in range(2, i):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + (i//j-1) + 1)

        # print(dp)
    
        return dp[n]