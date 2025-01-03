class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        l = nums[0]
        r = sum(nums) - l
        ans = 1 if l >= r else 0

        for i in range(1, len(nums)-1):
            l += nums[i]
            r -= nums[i]

            ans += 1 if l >=r else 0

        return ans
