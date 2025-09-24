class MyCalendar:

    def __init__(self):
        self.bookings_order = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.bookings_order:
            self.bookings_order.add([startTime, endTime])
            return True

        idx = bisect_right(self.bookings_order, [startTime, -inf])

        if idx:
            _, before_end = self.bookings_order[idx - 1]
            if startTime == 18:
                # print(self.bookings_order)
                # print(idx)
                # print(startTime, endTime)

            if idx < len(self.bookings_order):
                after_start, _ = self.bookings_order[idx]

                if before_end <= startTime and endTime <= after_start:
                    self.bookings_order.add([startTime, endTime])
                    return True
                
            elif before_end <= startTime:
                self.bookings_order.add([startTime, endTime])
                return True

        else:
            after_start, _ = self.bookings_order[idx]
            if endTime <= after_start:
                self.bookings_order.add([startTime, endTime])
                return True
        # print(self.bookings_order)

        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)