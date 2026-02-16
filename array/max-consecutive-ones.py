class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        count = 0
        for num in nums:
            count += (count + 1) * num - count 
            ans = max(ans, count)
        return ans