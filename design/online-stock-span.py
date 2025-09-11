class StockSpanner:

    def __init__(self):
        self.stock = []
        self.stack = []
        self.day = 0

    def next(self, price: int) -> int:
        
        while self.stack and self.stock[self.stack[-1]] <= price:
            self.stack.pop()

        ans = self.day - self.stack[-1] if self.stack else self.day + 1
        self.stack.append(self.day)
        self.stock.append(price)
        self.day += 1
        
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)