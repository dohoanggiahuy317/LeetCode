class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n

        for i in range(n):
            dp[i] = nums[i]
            for j in range(i - 1):
                dp[i] = max(dp[j] + nums[i], dp[i])

        # print(dp)
        
        return max(dp[-1], dp[-2])