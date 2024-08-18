class Solution:
    def checkValidString(self, s: str) -> bool:
        l = 0
        r = 0

        for i in s:
            if i == "(":
                l += 1
                r += 1

            if i == ")":
                l -= 1
                r -= 1
            
            if i == "*":
                l -= 1
                r += 1

            if r < 0:
                return False

            if l < 0:
                l += 1

        return 0 == l