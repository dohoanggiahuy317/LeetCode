class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, curr = 0, 0
        ans = inf

        for r, num in enumerate(nums):
            curr += nums[r]

            while curr >= target:
                ans = min(ans, r - l + 1)
                curr -= nums[l]
                l += 1

        return ans if ans != inf else 0