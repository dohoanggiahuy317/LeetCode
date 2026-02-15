class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr_idx = 0

        for i, num in enumerate(nums):
            if num != nums[curr_idx]:
                curr_idx += 1
                nums[curr_idx] = num
        
        return curr_idx + 1