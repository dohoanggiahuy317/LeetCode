class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2 == 1:
            return False

        target = s // 2

        nums.sort()

        dp = [False] * (target+1)
        dp[0] = True

        for x in nums:
            for i in range(target, -1, -1):
                if 0 <= i-x < target:
                    dp[i] = dp[i-x] or dp[i]
                
            print(x, dp)

        return dp[-1]
