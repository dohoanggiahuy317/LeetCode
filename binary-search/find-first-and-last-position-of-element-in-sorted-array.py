class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a, b = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target) - 1
        return [a, b] if (a < len(nums) and target == nums[a]) else [-1, -1]
