class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        seen = set()
        curr_sum = 0
        max_sum = 0

        for r, num in enumerate(nums):
            while num in seen:
                seen.remove(nums[l])
                curr_sum -= nums[l]
                l += 1
                
            seen.add(num)
            curr_sum += num

            max_sum = max(max_sum, curr_sum)

        return max_sum

