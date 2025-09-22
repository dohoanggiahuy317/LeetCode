class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev_freq = 0
        curr_char = ""
        curr_freq = 0
        ans = 0

        for char in s + " ":
            if char != curr_char:
                ans += min(prev_freq, curr_freq)
                prev_freq = curr_freq
                curr_freq = 1
                curr_char = char
            else:
                curr_freq += 1

        return ans