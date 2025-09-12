class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        ans = 0
        open_paren = 0

        for char in s:
            if char == "(":
                open_paren += 1
            else:
                if open_paren == 0:
                    ans += 1
                else:
                    open_paren -= 1
        
        return ans + open_paren