class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("INF")
        ans = 0

        for price in prices:
            if price < buy:
                buy = price
            else:
                ans = max(ans, price - buy)

        return ans