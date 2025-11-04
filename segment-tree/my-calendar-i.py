class MyCalendar:

    def __init__(self):
        self.events = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.events:
            self.events.add((startTime, endTime))
            return True

        l, r = 0, len(self.events) - 1
        idx = len(self.events)
        while l <= r:
            m = (l + r) // 2
            if endTime <= self.events[m][0]:
                idx = m
                r = m - 1
            else:
                l = m + 1

        prev_idx = idx - 1

        if idx == len(self.events) or idx != 0:
            if self.events[prev_idx][1] <= startTime:
                self.events.add((startTime, endTime))
                return True
            return False
        
        self.events.add((startTime, endTime))
        return True
  

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)