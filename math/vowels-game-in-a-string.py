class Solution:
    def doesAliceWin(self, s: str) -> bool:
        c = False
        for ch in list(s):
            if ch in "ueoai":
                c = True

        return c