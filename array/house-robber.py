class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n
        pref_max = [0] * n

        for i in range(n):
            dp[i] = nums[i] + (pref_max[i - 2] if i - 2 >= 0 else 0)
            pref_max[i] = max(dp[i], pref_max[i - 1])

        # print(dp)
        # print(pref_max)
        
        return max(dp[-1], dp[-2])