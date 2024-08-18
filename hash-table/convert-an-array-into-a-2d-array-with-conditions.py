class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()    
        
        d = {}
        maxf = 0
        
        for x in nums:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
            
            maxf = max(maxf, d[x])
        
        ans = []
        for i in range(maxf):
            ans.append([])
        
        for x, appr in d.items():
            start = 0
            while start < appr:
                ans[start].append(x)
                start += 1
        
        return ans
        