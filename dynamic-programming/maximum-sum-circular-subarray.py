class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        curr_max = nums[0]
        ans_max = nums[0]
        curr_min = nums[0]
        ans_min = nums[0]

        for i in range(1, len(nums)):
            curr_max = max(nums[i], curr_max + nums[i])
            ans_max = max(curr_max, ans_max)

            curr_min = min(nums[i], curr_min + nums[i])
            ans_min = min(curr_min, ans_min)

        if ans_min == sum(nums):
            return ans_max

        return max(ans_max, sum(nums) - ans_min)