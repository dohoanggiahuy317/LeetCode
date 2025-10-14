class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        ans = 1
        counter = Counter(s[0])
        l = 0

        for r in range(1, len(s)):
            counter[s[r]] += 1

            while counter[s[r]] > 1:
                counter[s[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)

        return ans