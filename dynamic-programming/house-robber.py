class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n

        for i in range(n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        # print(dp)
        # print(pref_max)
        
        return dp[-1]