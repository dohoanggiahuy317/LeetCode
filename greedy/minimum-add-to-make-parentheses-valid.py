class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        

        ans = 0
        stack = 0

        for char in s:
            if char == "(":
                stack += 1
            else:
                if stack == 0:
                    ans += 1
                else:
                    stack -= 1
        
        return ans + stack