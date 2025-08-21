class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        meets_num = len(meetings)

        occups_pq = [] # -> (end_time, room_idx)
        avail_pq = [i for i in range(n)] # -> room_idx
        i = time = 0
        room_count = Counter()

        # while còn meeting chưa được vô
        while occups_pq or i < meets_num:
            # Lấy ra hết các room end meeting và add vào available list
            while occups_pq and occups_pq[0][0] <= time:
                _, room_idx = heapq.heappop(occups_pq)
                heapq.heappush(avail_pq, room_idx)

            # add meetings đang chờ vào room cho đến khi hết available room, cập nhất occup_room
            while i < meets_num and meetings[i][0] <= time and avail_pq:
                room_idx = heapq.heappop(avail_pq)
                start, end = meetings[i]
                
                duration = end - start
                heapq.heappush(occups_pq, (time + duration, room_idx))
                room_count[room_idx] += 1
                i += 1

            # # nếu có occup_room có người, xét time gần nhất khi có meeting end
            # if occups_pq:
            #     time = occups_pq[0][0]
            time += 1

        rooms = [(-c, idx) for idx, c in room_count.items()]
        rooms.sort()

        return rooms[0][1]

        