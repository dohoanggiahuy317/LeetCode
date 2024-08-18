class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1
        
        
        count = 1
        x = 0
        while x < len(nums) - 1:
            if nums[x] < nums[x + 1]:
                count += 1
                ans = max(ans, count)
            else:
                count = 1
                
            x += 1
            
            
            
        count = 1
        x = 0
        while x < len(nums) - 1:
            if nums[x] > nums[x + 1]:
                count += 1
                ans = max(ans, count)
            else:
                count = 1
                
            x += 1
            
        return ans
            
            
        