class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0
        n = len(nums)

        dp = {}

        def bạck_track(i, prevSum):
            nonlocal n, nums, target, dp
            if i == n:
                if target == prevSum:
                    return 1
                return 0

            if (i, prevSum) in dp.keys():
                return dp[(i, prevSum)]

            dp[(i, prevSum)] = bạck_track(i+1, prevSum + nums[i]) + bạck_track(i+1, prevSum - nums[i])

            return dp[(i, prevSum)]


        return bạck_track(0, 0)