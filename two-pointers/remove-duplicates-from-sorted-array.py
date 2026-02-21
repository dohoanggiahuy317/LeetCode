class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        
        for i, num in enumerate(nums):
            if nums[k] != num:
                nums[k] = num
                k += 1

        return k