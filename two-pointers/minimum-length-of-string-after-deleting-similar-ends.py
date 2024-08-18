class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s) - 1

        while len(s) > 1 and s[0] == s[len(s) - 1]:
            s = s.strip(s[0])
            # print(s)


        return len(s)