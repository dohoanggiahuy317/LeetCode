class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = SortedList([i for i in range(n)])
        use_count = {i: 0 for i in range(n)}
        rooms_state = SortedList()

        for start, end in sorted(meetings):
            duration = end - start
            while rooms_state and rooms_state[0][0] <= start:
                _, room = rooms_state.pop(0)
                rooms.add(room)
            
            if not rooms:
                prev_end, room = rooms_state.pop(0)
                rooms.add(room)
                start = prev_end
            
            room = rooms.pop(0)
            rooms_state.add((start + duration, room))
            use_count[room] += 1

        ans = 0
        cur_max = 0    
        for i in range(n):
            if use_count[i] > cur_max:
                cur_max = use_count[i]
                ans = i

        return ans


