from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        chars = Counter()
        ans = 0

        while r < len(s):
            chars[ s[r] ] += 1

            while chars[ s[r] ] > 1:
                chars[ s[l] ] -= 1
                l += 1

            ans = max(ans, r - l + 1)
            r += 1
        
        return ans
