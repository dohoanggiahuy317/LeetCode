import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        end_time = max(list(map(lambda x: x[2], trips)))
        trips.sort(key = lambda x: x[1])
        curr_cap = 0
        queue = []

        for i in range(end_time):
            while queue and i >= queue[0][2]:
                curr_cap -= heapq.heappop(queue)[2]

            while trips and i <= trips[0][1]:
                curr_cap += trips[0][0]
                heapq.heappush(queue, (trips[0][2], trips[0][1], trips[0][0]))
                trips.pop(0)

            if curr_cap > capacity:
                return False

        return True
            