class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        
        dp = defaultdict(int, {0: 1})
        pref_sum = defaultdict(int, {0: 1})

        for i in range(1, n + 1):
            left = max(0, i - maxPts)
            right = min(k - 1, i - 1)

            dp[i] = max(0, pref_sum[right] - pref_sum[left - 1]) * 1/maxPts
            pref_sum[i] = pref_sum[i - 1] + dp[i]

        # print(dp)
        # print(pref_sum)
        # print()

        ans = 0
        for i in range(k, n + 1):
            ans += dp[i]

        return ans