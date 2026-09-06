class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.freq = defaultdict(list)

        for i, num in enumerate(arr):
            self.freq[num].append(i)
        

    def query(self, left: int, right: int, value: int) -> int:
        return bisect.bisect_right(self.freq[value], right) - bisect.bisect_left(self.freq[value], left) 


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)