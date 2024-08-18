class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        nums = list(filter(lambda x: x > 0, nums))
        # print(nums)
        if len(nums) == 0:
            return 1

        start = 1
        while start < len(nums) + 1:
            if start != nums[start-1]:
                return start
            start += 1
        
        return start