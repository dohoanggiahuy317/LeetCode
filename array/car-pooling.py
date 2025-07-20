class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key = lambda x: x[1])
        # print(trips)

        timestart = min([trip[1] for trip in trips])
        timeend = max([trip[2] for trip in trips])

        cur_guest = []
        cur_cap = 0
        cur_checkpoint = 0

        for cur_time in range(timestart, timeend + 1):
            while cur_guest and cur_guest[0][0] <= cur_time:
                _, num_guest = heapq.heappop(cur_guest)
                cur_cap -= num_guest

            while cur_checkpoint < len(trips) and trips[cur_checkpoint][1] <= cur_time:
                num_guest, st, en = trips[cur_checkpoint]
                heapq.heappush(cur_guest, (en, num_guest))
                cur_cap += num_guest
                cur_checkpoint += 1

            # print(cur_time, cur_cap)

            if cur_cap > capacity:
                return False
        
        return True