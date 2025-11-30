class MyCalendarTwo:

    def __init__(self):
        self.booked = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlaps:
            if max(s, start) < min(e, end):
                return False

        for s, e in self.booked:
            overlap_start = max(s, start)
            overlap_end = min(e, end)
            if overlap_start < overlap_end:
                self.overlaps.append((overlap_start, overlap_end))

        self.booked.append((start, end))
        return True