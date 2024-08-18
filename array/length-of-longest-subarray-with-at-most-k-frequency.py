class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l = 0
        r = -1
        
        d = {}
        ans = 0
        
        
        while r < len(nums)-1:
            
            r += 1
            if nums[r] in d:
                d[nums[r]] += 1
            else:
                d[nums[r]] = 1
            
            while d[nums[r]] > k:
                d[nums[l]] -= 1
                l += 1 
                
            ans = max(ans, r - l + 1)
            
        return ans