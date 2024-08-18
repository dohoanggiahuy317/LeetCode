class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        pos = 0
        ans = 0
        
        for i in nums:
            pos += i
            if pos == 0:
                ans += 1
                
        return ans