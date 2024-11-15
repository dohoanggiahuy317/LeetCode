class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return 0
            
        dp = [1] * len(arr)
        ans = float("INF")

        for i in range(1, len(arr)):
            for j in range(i-1, -1, -1):
                if arr[j] <= arr[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            
            ans = min(ans, (len(arr) - 1 - i) + (i + 1 - dp[i]) )

        # print(dp)
        return ans