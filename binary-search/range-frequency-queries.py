class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.N = len(arr)
        self.num2idx = defaultdict(list)
        for i, num in enumerate(arr):
            self.num2idx[num].append(i)

        # print(self.num2idx)
        

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.num2idx:
            return 0
        
        first_appear = bisect.bisect_left(self.num2idx[value], left)
        last_appear = bisect.bisect_right(self.num2idx[value], right) - 1

        # print(first_appear, last_appear)

        return last_appear - first_appear + 1


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)