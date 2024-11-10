class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        
        r = 0
        ans = 10 ** 15
        temp = []
        
        for r in range(len(nums)):
            curr = nums[r]
            
            for i in range(len(temp) - 1, -1, -1):
                curr = curr 
        
        if ans == 10**15:
            return -1
        return ans