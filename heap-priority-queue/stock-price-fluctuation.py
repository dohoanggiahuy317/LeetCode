class StockPrice:

    def __init__(self):
        self.price_set = SortedSet()
        self.today = 0
        self.time2price = {}

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.time2price:
            old_price = self.time2price[timestamp]
            self.price_set.remove((old_price, timestamp))

        self.today = max(self.today, timestamp)
        self.time2price[timestamp] = price
        self.price_set.add((price, timestamp))

    def current(self) -> int:
        return self.time2price[self.today]

    def maximum(self) -> int:
        return self.price_set[-1][0]

    def minimum(self) -> int:
        return self.price_set[0][0]
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()