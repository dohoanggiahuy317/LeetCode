class Solution:
    def removeDuplicates(self, nums):
        anchor_idx = 0

        for i, num in enumerate(nums):
            if nums[anchor_idx] != num:
                anchor_idx += 1
                nums[anchor_idx] = nums[i]

        return anchor_idx + 1