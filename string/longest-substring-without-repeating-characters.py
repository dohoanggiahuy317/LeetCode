class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        d = {}
        ans = 0
        l = 0

        for i in range(len(s)):
            if s[i] in d and d[s[i]] >= l:
                l = d[s[i]] + 1
            else:
                ans = max(ans, i - l + 1)
            d[s[i]] = i

        return ans