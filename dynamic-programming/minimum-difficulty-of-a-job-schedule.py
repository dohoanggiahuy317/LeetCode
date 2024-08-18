class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        return self.minDifficultyOptimized(jobDifficulty, d)

    def minDifficultyOptimized(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        if n < d:
            return -1
        elif n == d:
            return sum(jobDifficulty)  # Efficiently sum the difficulties

        # dp[j]: minimum difficulty of first (j+1) jobs in (i+1) days
        dp = [0] * n
        dp[0] = jobDifficulty[0]

        # Initialize dp with maximum difficulty encountered so far
        for i in range(1, n):
            dp[i] = max(jobDifficulty[i], dp[i - 1])

        dpPrev = [0] * n
        stack = []  # Use a list for the decreasing stack

        # Dynamic Programming with decreasing stack optimization
        for i in range(1, d):
            dp, dpPrev = dpPrev, dp  # Swap dp arrays concisely
            stack.clear()  # Clear the stack efficiently

            for j in range(i, n):
                dp[j] = jobDifficulty[j] + dpPrev[j - 1]

                # Process the decreasing stack
                while stack and jobDifficulty[stack[-1]] <= jobDifficulty[j]:
                    lastIdx = stack.pop()
                    dp[j] = min(dp[j], dp[lastIdx] + jobDifficulty[j] - jobDifficulty[lastIdx])

                if stack:
                    dp[j] = min(dp[j], dp[stack[-1]])

                stack.append(j)  # Append for clarity and efficiency

        return dp[n - 1]