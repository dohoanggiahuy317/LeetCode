class StockPrice:

    def __init__(self):
        self.time2stock = defaultdict(int)
        self.curr = []
        self.maxi = []
        self.mini = []
        

    def update(self, timestamp: int, price: int) -> None:
        self.time2stock[timestamp] = price
        heapq.heappush(self.curr, (-timestamp, price))
        heapq.heappush(self.maxi, (-price, timestamp))
        heapq.heappush(self.mini, (price, timestamp))

    def current(self) -> int:
        while self.time2stock[ -self.curr[0][0] ] != self.curr[0][1]:
            heapq.heappop(self.curr)
        return self.curr[0][1]
        
    def maximum(self) -> int:
        while self.time2stock[ self.maxi[0][1] ] != -self.maxi[0][0]:
            heapq.heappop(self.maxi)

        return -self.maxi[0][0]

    def minimum(self) -> int:
        while self.time2stock[ self.mini[0][1] ] != self.mini[0][0]:
            heapq.heappop(self.mini)

        return self.mini[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.curr()
# param_3 = obj.maximum()
# param_4 = obj.minimum()