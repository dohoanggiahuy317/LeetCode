class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1
        
        dp = {0:1}
        dp_s = {-1: 0, 0: 1}


        for i in range(1, n+1):
            s = dp_s[min(i - 1, k - 1)] - dp_s[max(i - maxPts - 1, -1)]
            if s < 0:
                s = 0
            dp[i] = s * (1/maxPts)
            dp_s[i] = dp_s[i - 1] + dp[i]

        ans = 0

        for i, v in dp.items():
            if i >= k:
                ans += v 


        return ans


