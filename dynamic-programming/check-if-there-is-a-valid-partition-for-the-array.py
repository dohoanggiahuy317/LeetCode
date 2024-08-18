class Solution:
    def validPartition(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return False

        if len(nums) < 3:
            if nums[0] == nums[1]:
                return True
            return False


        dp = [False] * len(nums)

        if nums[0] == nums[1]:
            dp[1] = True
            if nums[2]==nums[1]:
                dp[2] = True
        elif nums[0]+1==nums[1]:
            if nums[2]==nums[1] or nums[2]==nums[1]+1:
                dp[2] = True


        for i in range(3, len(nums)):
            c1 = (dp[i-3] == True) and (nums[i]==nums[i-1]==nums[i-2] or nums[i]==nums[i-1]+1==nums[i-2]+2)
            c2 = (dp[i-2] == True) and (nums[i]==nums[i-1])

            if c1 or c2:
                dp[i] = True

        return dp[-1]
        