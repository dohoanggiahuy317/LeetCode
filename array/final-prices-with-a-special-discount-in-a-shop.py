class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        ans = prices[:]

        for i, price in enumerate(prices):
            while stack and stack[-1][1] >= price:
                ci, cprice = stack.pop()
                ans[ci] -= price

            stack.append((i, price))

        return ans