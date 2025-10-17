class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        prefix_min = [inf] * n
        prefix_min[0] = prices[0]

        ans = 0
        for i, price in enumerate(prices[1:]):
            ans = max(ans, price - prefix_min[i - 1])
            prefix_min[i] = min(price, prefix_min[i - 1])

        return ans


        