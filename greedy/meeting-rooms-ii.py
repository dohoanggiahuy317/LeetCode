class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        line = []

        for start, end in intervals:
            line.append([start, 1])
            line.append([end, -1])

        ans = -inf
        room_count = 0
        line.sort()

        for _, action in line:
            room_count += action
            ans = max(ans, room_count)

        return ans