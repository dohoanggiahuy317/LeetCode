from collections import Counter

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1 or len(nums) == 1:
            return False

        target = s // 2
        dp = [False] * (target + 1)
        dp[0] = True
        curr_sum = 0

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
            

        # print(dp)

        return dp[-1]