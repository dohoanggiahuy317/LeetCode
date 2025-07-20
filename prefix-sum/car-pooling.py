class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_destination = max([tr[2] for tr in trips])
        pad_count = [0] * (max_destination + 1)

        for num, st, en in trips:
            for i in range(st, en):
                pad_count[i] += num

        return all(co <= capacity for co in pad_count)