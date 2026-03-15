class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i, num in enumerate(nums):
            if num == 0:
                first_zero_idx = i
                break
        else:
            return nums
        
        for i, num in enumerate(nums[first_zero_idx:]):
            if num != 0:
                nums[i], nums[first_zero_idx] = nums[first_zero_idx], nums[i]
                first_zero_idx += 1

        return nums