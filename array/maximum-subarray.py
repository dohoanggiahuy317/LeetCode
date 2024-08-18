class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        ans = nums[0]
        curr = nums[0]

        for i in range(1, len(nums)):
            if curr < 0:
                curr = 0
            curr += nums[i]
            ans = max(ans, curr)


        return ans