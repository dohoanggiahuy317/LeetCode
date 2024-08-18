class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        d={}
        
        for x in nums:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
                
        ans = 0
        
        for u, v in d.items():
            if v == 2:
                ans = ans ^ u
                
        return ans