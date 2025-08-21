class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        meets_num = len(meetings)

        occups_pq = [] # -> (end_time, room_idx)
        avail_pq = [i for i in range(n)] # -> room_idx
        i = curr_time = 0
        room_count = Counter()

        # while còn meeting chưa được vô
        while occups_pq or i < meets_num:
            # Lấy ra hết các room end meeting và add vào available list
            while occups_pq and occups_pq[0][0] <= curr_time:
                _, room_idx = heapq.heappop(occups_pq)
                heapq.heappush(avail_pq, room_idx)

            # add meetings đang chờ vào room cho đến khi hết available room, cập nhất occup_room
            while i < meets_num and meetings[i][0] <= curr_time and avail_pq:
                room_idx = heapq.heappop(avail_pq)
                start, end = meetings[i]
                
                duration = end - start
                heapq.heappush(occups_pq, (curr_time + duration, room_idx))
                room_count[room_idx] += 1
                i += 1
            
            print(curr_time, occups_pq)
            # Có free room cho next meeting, nhảy đến curr_time đó và loop sẽ remove các meeting done
            if avail_pq and i < meets_num:
                curr_time = meetings[i][0]
            # nếu ko có room nào avail, xét curr_time mà room tiếp theo avail
            elif occups_pq:
                curr_time = occups_pq[0][0]
            # tăng
            # else:
            #     curr_time = max(time, meetings[i][0]) if i < meets_num else (occups_pq[0][0] if occups_pq else curr_time + 1)
            

        rooms = [(-c, idx) for idx, c in room_count.items()]
        rooms.sort()

        return rooms[0][1]

        