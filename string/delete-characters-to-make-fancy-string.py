class Solution:
    def makeFancyString(self, s: str) -> str:
        st, en = 0, 0
        temp, ans = 0, ""

        while en < len(s):
            while en < len(s) and s[st] == s[en]:
                temp += 1
                en += 1
            ans += min(2, temp) * s[st]
            temp = 0
            st = en


        return ans