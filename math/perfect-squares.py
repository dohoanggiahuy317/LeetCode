class Solution:
    def numSquares(self, n: int) -> int:
        if sqrt(n) == int(sqrt(n)):
            return 1

        dp = {0: 0}
    
        for j in range(n+1):
            dp[j] = 99999
            if sqrt(j) == int(sqrt(j)):
                dp[j] = 1
            for i in range( int(sqrt(j))+1 ):
                dp[j] = min(dp[j], dp[ j - i*i ] + 1)

        return dp[n]



        

        