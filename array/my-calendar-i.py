class MyCalendar:

    def __init__(self):
        self.events = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.events:
            self.events.add((startTime, endTime))
            return True

        idx = bisect.bisect_left(self.events, (endTime, -1))
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