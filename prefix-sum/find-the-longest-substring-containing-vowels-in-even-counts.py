class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        VOWELS = "ueoai"

        def valid_string(s, k):
            for i in range(len(s) - k + 1):
                freq = Counter(s[i: i + k])
                if all(freq[c] % 2 == 0 for c in VOWELS):
                    return True
            
            return False

        l, r = 0, len(s)
        ans = 0
        while l <= r:
            m = (l + r) >> 1

            if valid_string(s, m):
                ans = m
                l = m + 1
            else:
                r = m - 1

        return ans