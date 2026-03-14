class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = []
        
        for i, num in enumerate(nums):
            arr.append(arr[-1] + num)

        return arr