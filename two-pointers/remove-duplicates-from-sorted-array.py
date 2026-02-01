class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        anchor_idx = 0
        count = 0

        for i, num in enumerate(nums):
            if num == nums[anchor_idx] and i != anchor_idx:
                nums[i] = inf
            else:
                anchor_idx = i
                count += 1

        nums.sort()
        return count