class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for num in nums:
            if num != nums[k]:
                nums[k + 1] = num
                k += 1
        return k + 1
