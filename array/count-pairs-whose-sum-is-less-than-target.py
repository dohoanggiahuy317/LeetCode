class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        count = 0
        while i < j:
            while nums[i] + nums[j] >= target:
                j -= 1
            count += max(0, j - i)
            i += 1
            
        return count