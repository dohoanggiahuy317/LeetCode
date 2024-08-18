class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        dp = {}

        def solve(currDay):
            if currDay >= len(days):
                return 0
            if currDay in dp:
                return dp[currDay]

            dp[currDay] = 10 ** 9
            for d, c in zip([1, 7, 30], costs):
                day_iter = currDay
                while day_iter < len(days) and days[day_iter] < days[currDay] + d:
                    day_iter += 1
                dp[currDay] = min(dp[currDay], solve(day_iter) + c)

            return dp[currDay]

        
        return solve(0)
