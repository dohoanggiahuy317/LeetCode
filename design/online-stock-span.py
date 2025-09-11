class StockSpanner:

    def __init__(self):
        self.idx_stock = []
        self.day = 0

    def next(self, price: int) -> int:
        
        while self.idx_stock and self.idx_stock[-1][1] <= price:
            self.idx_stock.pop()

        ans = self.day - self.idx_stock[-1][0] if self.idx_stock else self.day + 1
        self.idx_stock.append((self.day, price))
        self.day += 1
        
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)