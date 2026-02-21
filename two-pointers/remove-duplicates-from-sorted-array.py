class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        
        for num in nums:
            if nums[k] != num:
                k += 1
                nums[k] = num

        return k + 1