class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = {len(questions): 0}

        for i in range(len(questions)-1, -1, -1):
            dp[i] = 0
            p, b = questions[i]
            add_p = 0
            if (i + b + 1) < len(questions):
                add_p = dp[min(i + b + 1, len(questions))]
            dp[i] = max(add_p + p, dp[i+1])

        # def solve(i):
        #     if i >= len(questions):
        #         return 0
        #     if i in dp:
        #         return dp[i]

        #     dp[i] = 0
        #     p, b = questions[i]
        #     dp[i] = max(solve(i+b+1) + p, solve(i+1))

        #     return dp[i]

        # solve(0)
        # print(dp)
        return dp[0]
        