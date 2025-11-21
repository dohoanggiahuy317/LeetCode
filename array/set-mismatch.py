class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i, num in enumerate(nums):
            if num != i + 1:
                return [i, i + 1]
        