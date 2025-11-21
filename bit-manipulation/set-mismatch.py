class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            if num != i + 1:
                return [i, i + 1]
        