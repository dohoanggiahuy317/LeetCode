class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        ns = ""
        for i in range(len(s)):
            if i == 0 and s[i] in "+-":
                ns += s[i]
            elif s[i].isdigit():
                ns += s[i]
            else:
                break

        if not ns or ns in "+-":
            return 0

        ans = int(ns)
        

        if ans > 2 ** 31 - 1:
            ans = 2 ** 31 - 1
        if ans < - 2 ** 31:
            ans = - 2 ** 31

        return ans