class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        largest_end = max([x[2] for x in trips])
        track = [0] * (largest_end + 1)

        for num, f, t in trips:
            for i in range(f, t):
                track[i] += num

        return all(x <= capacity for x in track)