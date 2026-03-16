class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        j = len(nums) - 1
        count = 0
        for i, num in enumerate(nums):
            while i < j and nums[i] + nums[j] >= target:
                j -= 1
            count += max(0, j - i)
            
        return count