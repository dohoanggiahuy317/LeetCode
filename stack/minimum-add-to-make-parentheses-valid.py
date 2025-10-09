class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        curr_open = 0

        for paren in s:
            if paren == "(":
                curr_open += 1
            else:
                curr_open -= 1
            
            if curr_open < 0:
                ans += 1
                curr_open = 0

        return ans + curr_open