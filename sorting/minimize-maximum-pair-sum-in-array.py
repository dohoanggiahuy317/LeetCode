class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        ans = 0

        while l < r:
            ans = max(ans, nums[l] + nums[r])
            r -= 1
            l += 1

        return ans