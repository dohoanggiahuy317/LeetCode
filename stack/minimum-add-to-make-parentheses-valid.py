class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l = 0
        ans = 0

        for char in list(s):
            if char == "(":
                l += 1
            else:
                l -= 1
            
            if l < 0:
                ans += 1
                l = 0
        
        return ans + abs(l)