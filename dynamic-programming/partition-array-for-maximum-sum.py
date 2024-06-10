class Solution:
    def maxSumAfterPartitioning(self, arr, k):

        arr = [0] + arr
        dp = [0] * (len(arr))
        curr_max = max(arr[:k])
        dp[1] = arr[1]

        for i in range(2, len(arr)):
            curr = 0  
            for x in range(k):
                curr = max(
                    curr, 
                    dp[max(0, i-1 - x)] + 
                        (x+1 if i-x > 0 else i) * max(arr[max(0, i-x): i+1])      
                    )

            dp[i] = max(dp[i], curr)
        return dp[-1]


