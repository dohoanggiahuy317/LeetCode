class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        for i in range(len(nums) - 1):
            if nums[i] != nums[i+1] and nums[i] != nums[i-1]:
                return nums[i]
        else:
            return nums[len(nums) - 1]