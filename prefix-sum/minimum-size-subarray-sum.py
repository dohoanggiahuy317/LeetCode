class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        r = 0
        curr_sum = 0
        ans = inf

        for l, num in enumerate(nums):
            if curr_sum >= target:
                ans = min(ans, r - l + 1)
                curr_sum -= nums[l]
            else:
                while r < len(nums) - 1 and curr_sum < target:
                    r += 1
                    curr_sum += nums[r]

            # print(l, r, curr_sum)

        return 0 if ans == inf else ans