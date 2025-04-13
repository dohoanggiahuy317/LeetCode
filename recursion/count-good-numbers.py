class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even = (n+1)//2
        odd = n // 2
        MOD = 10**9 + 7

        return (((5 ** (even)) % MOD) * ((4 ** (odd)) % MOD)) % MOD