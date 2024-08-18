class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        currmax = 0
        ans = 0
        
        for x, y in dimensions:
            if x**2 + y**2 > currmax:
                currmax = x**2 + y**2
                ans = x*y
            elif x**2 + y**2 == currmax:
                ans = max(ans, x*y)
                
        return ans