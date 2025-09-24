class MyCalendar:

    def __init__(self):
        self.bookings_order = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:

        if not self.bookings_order:
            self.bookings_order.add([startTime, endTime])
            return True
        
        n = len(self.bookings_order)
        idx = bisect_right(self.bookings_order, [startTime, 0])

        previous_end = self.bookings_order[idx - 1][1] if idx > 0 else -inf
        after_start = self.bookings_order[idx][0] if idx < n else inf

        if  previous_end <= startTime and endTime <= after_start:
            self.bookings_order.add([startTime, endTime])
            return True

        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)