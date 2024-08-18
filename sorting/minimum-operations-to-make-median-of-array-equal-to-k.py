class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        
        
        nums.sort()
        
        mid = nums[ len(nums)//2 ]
        
        
        if k == mid:
            return 0
        
        
        ans = 0
        s = len(nums)//2
        ite = s
        
        if mid < k:

            while ite < len(nums) and nums[ite] < k:
                ite += 1
            
            for i in range(s, ite):
                ans += k - nums[i]
                
        elif mid > k:

            while ite >= 0 and nums[ite] > k:
                ite -= 1
                
            # print(ite, s)
                            
            for i in range(ite + 1, s + 1):
                ans += nums[i] - k
                
        
        return ans
            
            
            
            
            
            
            