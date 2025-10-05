class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False

        target = s // 2
        dp = [False] * (target + 1)

        dp[0] = True
        
        for num in nums:
            for i in range(target + 1, -1, -1):
                if i + num < target + 1:
                    dp[i + num] = dp[i] or dp[i + num]
            # print(dp)

        return dp[-1]