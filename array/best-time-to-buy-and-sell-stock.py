class Solution:
    def maxProfit(prices):
        min_price, max_profit = float('inf'), 0
        for p in prices:
            if p < min_price:
                min_price = p
            elif p - min_price > max_profit:
                max_profit = p - min_price
        return max_profit

    with open('user.out', 'w') as f:
        for case in map(loads, stdin):
            f.write(f"{maxProfit(case)}\n")
    exit(0)  