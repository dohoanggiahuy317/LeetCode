class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        line = [0] * (n + 2)

        for f, l, s in bookings:
            line[f] += s
            line[l + 1] -= s

        return list(accumulate(flights))[1:-1]