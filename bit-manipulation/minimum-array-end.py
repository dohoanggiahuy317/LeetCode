class Solution:
    def minEnd(self, n: int, x: int) -> int:
        binx = bin(x)[2:]
        binn1 = bin(n-1)[2:]
        ans = ""

        for i, bit in enumerate(binx[::-1]):
            if bit == "1":
                ans += "1"
            else:
                if binn1:
                    ans += binn1[-1]
                    binn1 = binn1[:-1]

        ans = binn1 + ans

        return int(ans, 2)
