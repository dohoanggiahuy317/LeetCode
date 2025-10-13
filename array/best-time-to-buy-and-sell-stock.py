class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        prefix_min = [prices[0]] * n
        suffix_max = [prices[-1]] * n

        for i in range(1, n):
            prefix_min[i] = min(prefix_min[i - 1], prices[i])

        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], prices[i])
        
        ans = 0
        for i in range(n):
            ans = max(ans, suffix_max[i] - prefix_min[i])
        
        return ans