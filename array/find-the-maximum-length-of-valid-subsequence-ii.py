class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = defaultdict(int)
        ans = 0

        for num in nums:
            remainder = num % k

            for prev in range(k):
                dp[(remainder, prev)] = dp[(prev, remainder)] + 1
                ans = max(ans, dp[(remainder, prev)])
        
        return ans