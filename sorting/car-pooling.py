class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key = lambda x: x[1])

        timestart = min([trip[1] for trip in trips])
        timeend = max([trip[2] for trip in trips])

        cur_guest = deque()
        cur_cap = 0
        cur_checkpoint = 0

        for cur_time in range(timestart, timeend + 1):
            while cur_guest and cur_guest[0][1] <= cur_time:
                num_guest, _ = cur_guest.popleft()
                cur_cap -= num_guest

            while cur_checkpoint < len(trips) and trips[cur_checkpoint][1] >= cur_time:
                num_guest, st, en = trips[cur_checkpoint]
                cur_guest.append((num_guest, en))
                cur_cap += num_guest
                cur_checkpoint += 1

            if cur_cap > capacity:
                return False
        
        return True