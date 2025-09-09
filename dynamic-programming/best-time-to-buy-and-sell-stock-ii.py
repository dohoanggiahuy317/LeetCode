class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        for prev, after in pairwise(prices):
            if prev < after:
                ans += after - prev

        return ans
                