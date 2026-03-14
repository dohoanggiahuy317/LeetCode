class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = []
        
        for i, num in enumerate(nums):
            arr.append(arr[-1] if arr else 0 + num)

        return arr