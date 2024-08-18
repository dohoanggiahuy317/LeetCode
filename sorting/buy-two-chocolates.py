class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()

        a = money - prices[0] - prices[1]

        if a >= 0:
            return a
        else:
            return money
