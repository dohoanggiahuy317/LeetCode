class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1
        # dp[i] = prob reach score i
        # dp[i] = sum(dp[i-maxPts] -> dp[i-1]) * 1/maxPts
        # dp[i] = (pref_sum[i-1] - pref_sum[i-maxPts - 1]) * 1/maxPts
       
        dp = defaultdict(int, {0: 1}) # starts at 0 so prob at 0 is 1
        pref_sum = defaultdict(int, {0: 1}) # pref_sum of dp

        for i in range(1, n + 1):
            largest = min(i - 1, k - 1)
            smallest = i - maxPts - 1
            prev_prob = pref_sum[largest] - (pref_sum[smallest] if smallest >= 0 else 0)

            prob_i = (prev_prob) * 1/maxPts
            
            dp[i] = prob_i
            pref_sum[i] = pref_sum[i - 1] + prob_i

        
        ans = 0
        for i in range(k, n+1):
            ans += dp[i]

        return ans