class Solution:
    def countVowelStrings(self, n: int) -> int:
    
        def backtrack(curr,t):
            nonlocal ans

            if curr == n:
                ans += 1
                return
            if t >= 5:
                return 
            backtrack(curr+1, t)
            backtrack(curr, t+1)

        ans = 0
        backtrack(0, 0)
        return ans