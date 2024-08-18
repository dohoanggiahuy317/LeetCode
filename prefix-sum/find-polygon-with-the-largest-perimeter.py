class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return False
        
        nums.sort()
        
        curr = sum(nums)
        start = len(nums) - 1
        end = 0
        
        ans = -1
        
            
        while curr <= 2 * nums[start]:  
            l = []
            for x in range(end, start+1):
                l.append(nums[x])
            print(l)
            curr -= nums[start]
            start -= 1
            
            if start < end + 2:
                return -1
            
            
            
    

                
        return curr
            