class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        DICT_MAP = {chr(i + ord("a")): i for i in range(26)}

        forward = 0
        backward, power = 0, 1
        longest = 0

        for i, ch in enumerate(s):
            forward = forward * 26 + DICT_MAP[ch]
            backward = DICT_MAP[ch] * power + backward
            power = power * 26

            if forward == backward:
                longest = i + 1    

        suffix = s[longest:]
        return suffix[::-1] + s