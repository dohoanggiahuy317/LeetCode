class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        ad = False
        val = -1

        for i in range(len(s)):
            if not ad and spaces:
                ad = True
                val = spaces.pop(0)

            if ad and i == val:
                ad = False
                ans += " "
            ans += s[i]

        return ans