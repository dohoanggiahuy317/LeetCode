class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        
        dp = [1] * len(nums)

        for i, num in enumerate(nums):
            for j in range(0, i):
                dp[i] = max(dp[i], dp[j] + 1 if nums[j] + k >= num > nums[j] else 0)

        return max(dp)