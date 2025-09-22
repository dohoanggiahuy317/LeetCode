class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 1
        l, r = 0, 1
        tracker = Counter(s[0])

        while r < len(s):
            while l < len(s) and tracker[s[r]] > 0:
                char = s[l]
                tracker[char] -= 1
                l += 1
            
            tracker[s[r]] += 1
            ans = max(r - l + 1, ans)
            r += 1

        return ans