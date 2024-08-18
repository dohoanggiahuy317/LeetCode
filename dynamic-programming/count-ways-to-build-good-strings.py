class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        mod = 10 ** 9 + 7

        def solve(i):
            if i > high:
                return 0
            
            if i in dp:
                return dp[i]

            ans = 0
            if i + zero <= high:
                ans += solve(i + zero)
            if i + one <= high:
                ans += solve(i + one)
            
            dp[i] = ans % mod
            return dp[i]

        dp = {high: 1}

        res = 0
        for x in range(high - low + 1):
            res += solve(x)
            res = res % mod

        return res
          

    