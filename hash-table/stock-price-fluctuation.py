class SegmentTree:
    def __init__(self, nums, func, given):
        self.N = len(nums)
        self.func = func
        self.given = given

        self.tree = [given] * (self.N * 2)
        self.tree[self.N:] = nums
        
        for i in range(self.N - 1, 0, -1):
            self.tree[i] = self.func(self.tree[i << 1], self.tree[(i << 1) | 1])
    
    def update(self, i, val):
        i += self.N
        self.tree[i] = val
        while i > 1:
            self.tree[i >> 1] = self.func(self.tree[i], self.tree[i ^ 1])
            i >>= 1
    
    def query(self, l, r):
        l += self.N
        r += self.N
        ans = self.given
        
        while l < r:
            if (l & 1):
               ans = self.func(self.tree[l], ans)
               l += 1
            if r & 1:
                r -= 1
                ans = self.func(self.tree[r], ans)
                
            l >>= 1
            r >>= 1

        return ans


class StockPrice:

    def __init__(self):
        self.min_tree = SegmentTree([inf] * (10 ** 5), min, inf)
        self.max_tree = SegmentTree([-inf] * (10 ** 5), max, -inf)
        self.curr = 0
        self.tracker = defaultdict(int)

    def update(self, timestamp: int, price: int) -> None:
        self.curr = max(self.curr, timestamp)
        self.tracker[timestamp] = price
        self.min_tree.update(timestamp, price)
        self.max_tree.update(timestamp, price)
        print(self.min_tree.tree[-10:])

    def current(self) -> int:
        return self.tracker[self.curr]

    def maximum(self) -> int:
        return self.max_tree.query(0, self.curr + 1)

    def minimum(self) -> int:
        return self.min_tree.query(0, self.curr + 1)
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()