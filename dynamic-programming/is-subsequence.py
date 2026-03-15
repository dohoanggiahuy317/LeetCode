class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0

        for char in t:
            if char == s[i]:
                i += 1
        
        return i == len(s)