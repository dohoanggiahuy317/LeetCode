class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = 0, 1

        for i, num in enumerate(nums):
            if num % 2 == 0 and i % 2 != 0:
                nums[i], nums[even] = nums[even], nums[i]
                even += 2
            elif num % 2 != 0 and i % 2 == 0:
                nums[i], nums[odd] = nums[odd], nums[i]
                odd += 2

        return nums
