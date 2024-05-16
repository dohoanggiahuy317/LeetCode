class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for i in range(26):
            char = chr(i + ord("a"))
            if char in s:
                fi = s.index(char)
                la = s.rindex(char)

                if fi != la:
                    rest = set()
                    for x in list(s[fi + 1:la]):
                        rest.add(x)
                    ans += len(rest)

        return ans