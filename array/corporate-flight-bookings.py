class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        lines = [0] * (n + 2)

        for f, l, s in bookings:
            lines[f] += s
            lines[l + 1] -= s

        return list(accumulate(lines))[1:-1]