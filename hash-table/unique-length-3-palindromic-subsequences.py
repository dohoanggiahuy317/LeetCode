class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0

        for i in range(26):
            char = chr(i + ord("a"))

            if char in s:
                l, r = s.index(char), s.rindex(char)

                if r != l:
                    ans += len(set(list(s[l+1: r])))
        
        return ans
