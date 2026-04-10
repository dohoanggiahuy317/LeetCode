class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        freq = Counter()
        ans = 0

        for r, char in enumerate(s):
            freq[char] += 1

            while len(freq) == 3:
                freq[s[l]] -= 1

                if freq[s[l]] == 0:
                    del freq[s[l]]

                l += 1

                ans += len(s) - r

        return ans
            