class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False

        target = s // 2
        dp = [False] * (target + 1)

        dp[0] = True
        
        for i in range(target + 1):
            for num in nums:
                if i + num < target + 1:
                    dp[i + num] = dp[i + num] or dp[i]

        return dp[-1]