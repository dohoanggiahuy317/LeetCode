class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            ans += sum( nums[ max(0, i - nums[i]) : i+1 ])

        return ans