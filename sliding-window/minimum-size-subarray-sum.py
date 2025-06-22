class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("INF")
        curr_sum, left = 0, 0

        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                curr_sum -= nums[left]
                left += 1
                ans = min(ans, right - left + 2)
        
        return ans if ans != float("INF") else 0
