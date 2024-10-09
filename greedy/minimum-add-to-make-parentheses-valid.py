class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l = 0

        for char in list(s):
            if char == "(":
                l += 1
            else:
                l -= 1
        
        return abs(l)