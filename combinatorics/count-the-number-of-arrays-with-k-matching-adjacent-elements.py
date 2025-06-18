MOD = 10**9 + 7

class Solution:
    def mod_inverse(self, a, mod):
        res = 1
        power = mod - 2
        while power:
            if power & 1:
                res = res * a % mod
            a = a * a % mod
            power >>= 1
        return res

    def nCr(self, n, r):
        if r > n:
            return 0
        if r == 0 or r == n:
            return 1

        res = 1
        for i in range(1, r + 1):
            res = res * (n - r + i) % MOD
            res = res * self.mod_inverse(i, MOD) % MOD
        return res

    def bin_expo(self, a, b):
        result = 1
        while b:
            if b & 1:
                result = result * a % MOD
            a = a * a % MOD
            b >>= 1
        return result

    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        formula = m * self.bin_expo(m - 1, n - (k + 1)) % MOD
        updated_formula = formula * self.nCr(n - 1, k) % MOD
        return updated_formula
