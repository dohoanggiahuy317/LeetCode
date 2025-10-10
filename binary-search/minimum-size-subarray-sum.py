class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        r = 0
        curr_sum = 0
        ans = inf

        for l, num in enumerate(nums):
            curr_sum -= nums[l - 1] if l - 1 >= 0 else 0

            while r < len(nums) and curr_sum < target:
                curr_sum += nums[r]
                r += 1
            
            if curr_sum >= target:
                ans = min(ans, r - l )

        return 0 if ans == inf else ans