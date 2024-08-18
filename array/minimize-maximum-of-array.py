class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        ans = nums[0]
        prefSum = 0

        for i in range(len(nums)):
            prefSum += nums[i]
            ans = max(ans, ceil( prefSum/(i+1) ))

        return ans