class MyCalendar:

    def __init__(self):
        self.li = []
        

    def book(self, start: int, end: int) -> bool:
        b = True

        for x in self.li:
            if x[1] <= start or x[0] >= end:
                continue
            else:
                b = False
                break

        if b:
            self.li.append((start, end))
        return b


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)