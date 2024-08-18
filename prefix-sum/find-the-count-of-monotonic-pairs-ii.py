from functools import lru_cache
from typing import List

class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        dp = [[0] * (max(nums) + 1) for _ in range(n)]
        prefix_sum = [[0] * (max(nums) + 1) for _ in range(n)]
        
        for j in range(nums[0] + 1):
            dp[0][j] = 1 
            prefix_sum[0][j] = (prefix_sum[0][j-1] + dp[0][j]) if j > 0 else dp[0][j]

        for i in range(1, n):
            for j in range(nums[i] + 1):
                arr2_i = nums[i] - j

                if arr2_i >= 0:

                    max_valid_k = min(j, nums[i-1] - arr2_i)
                    if max_valid_k >= 0:
                        dp[i][j] = prefix_sum[i-1][max_valid_k] % MOD
                
                prefix_sum[i][j] = (prefix_sum[i][j-1] + dp[i][j]) % MOD if j > 0 else dp[i][j]

        return sum(dp[n-1][j] for j in range(nums[-1] + 1)) % MOD