class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cou = set()
        ans = 0
        l = 0

        for r in range(len(s)):
            if s[r] not in cou:
                cou.add(s[r])
                ans = max(ans, len(cou))

            else:
                while l < r and s[l] != s[r]:
                    cou.remove(s[l])
                    l += 1

                l += 1

        return ans
