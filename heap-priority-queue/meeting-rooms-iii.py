class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = [i for i in range(n)]
        use_count = {i: 0 for i in range(n)}
        rooms_state = []

        for start, end in sorted(meetings):
            duration = end - start
            while rooms_state and rooms_state[0][0] <= start:
                _, room = heapq.heappop(rooms_state)
                heapq.heappush(rooms, room)
            
            if not rooms:
                prev_end, room = heapq.heappop(rooms_state)
                heapq.heappush(rooms, room)
                start = prev_end
            
            room = heapq.heappop(rooms)
            heapq.heappush(rooms_state, (start + duration, room))
            use_count[room] += 1

        ans = 0
        cur_max = 0    
        for i in range(n):
            if use_count[i] > cur_max:
                cur_max = use_count[i]
                ans = i

        return ans


