class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ans = 0

        d = {}
        for char in list(s):
            if char in d:
                d[char] += 1
            else:
                d[char] = 1

        for char in list(t):
            if char in d:
                if d[char] == 0:
                    ans += 1
                else:
                    d[char] -= 1
            else:
                ans += 1
        
        return ans