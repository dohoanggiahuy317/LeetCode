class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                dp[i] = max(dp[i], (dp[j] + 1) if nums[j] < nums[i] else 0)
        
        return max(dp)