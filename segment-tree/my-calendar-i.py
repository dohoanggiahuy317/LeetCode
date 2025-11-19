class MyCalendar:

    def __init__(self):
        self.calender = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.calender:
            self.calender.add((startTime, endTime))
            return True

        n = len(self.calender)
        l, r = 0, n - 1
        idx = -1
        while l <= r:
            m = (l + r) >> 1
            if self.calender[m][0] <= startTime:
                idx = m
                l = m + 1
            else:
                r = m - 1 
        
        if idx == len(self.calender) - 1:
            if self.calender[idx][1] <= startTime:
                self.calender.add((startTime, endTime))
                return True

        if idx == -1:
            if self.calender[idx + 1][0] >= endTime:
                self.calender.add((startTime, endTime))
                return True

        after_idx = idx + 1
        if self.calender[idx][1] <= startTime and endTime <=  self.calender[after_idx][1]:
            self.calender.add((startTime, endTime))
            return True

        return False
        



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)