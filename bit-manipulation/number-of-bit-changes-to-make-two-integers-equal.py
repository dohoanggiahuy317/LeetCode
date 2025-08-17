class Solution:
    def minChanges(self, n: int, k: int) -> int:
        bn = bin(n)[2:]
        bk = bin(k)[2:]

        if len(bn) < len(bk):
            return -1
        
        bk = "0" * (len(bn) - len(bk)) + bk

        ans = 0
        for i in range(len(bn)):
            if bn[i] == "1" and bk[i] == "0":
                ans += 1
            elif bn[i] == "0" and bk[i] == "1":
                return -1

        return ans