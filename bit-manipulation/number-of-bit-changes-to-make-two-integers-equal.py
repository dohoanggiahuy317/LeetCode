class Solution:
    def minChanges(self, n: int, k: int) -> int:
        bin_n = bin(n)[2:]
        bin_k = bin(k)[2:]

        t = max(len(bin_n), len(bin_k))

        bin_n = "0" * (t - len(bin_n)) + bin_n
        bin_k = "0" * (t - len(bin_k)) + bin_k

        # print(bin_n, bin_k)
        ans = 0
        for i in range(t):
            if bin_n[i] == "1" and bin_k[i] == "0":
                ans += 1
            elif bin_n[i] == "0" and bin_k[i] == "1":
                return -1
        return ans