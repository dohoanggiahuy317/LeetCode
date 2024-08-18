class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        li = list(  sorted(zip(ages, scores), key=lambda x: (x[0], x[1])  ))

        dp = [0] * (len(li) + 1)

        for i, x in enumerate( li ):
            dp[i+1] = x[1]

            for prev in range(i-1, -1, -1):
                if x[1] >= li[prev][1]:
                    dp[i+1] = max( dp[i+1], dp[prev+1] + x[1] )

        return max(dp)