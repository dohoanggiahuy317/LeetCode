class SummaryRanges:

    def __init__(self):
        self.intervals = SortedList()

    def addNum(self, value: int) -> None:
        if not self.intervals:
            self.intervals.add([value, value])
            return
        
        after_idx = bisect_right(self.intervals, [value, inf])
        before_idx = after_idx - 1

        if before_idx >= 0 and self.intervals[before_idx][0] <= value <= self.intervals[before_idx][1]:
            return

        curr_start, curr_end = value, value
        if after_idx < len(self.intervals) and self.intervals[after_idx][0] == value + 1:
            curr_end = self.intervals[after_idx][1]
            self.intervals.pop(after_idx)

        if before_idx >= 0 and self.intervals[before_idx][1] == value - 1:
            curr_start = self.intervals[before_idx][0]
            self.intervals.pop(before_idx)

        self.intervals.add([curr_start, curr_end])

    def getIntervals(self) -> List[List[int]]:
        return list(self.intervals)


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()