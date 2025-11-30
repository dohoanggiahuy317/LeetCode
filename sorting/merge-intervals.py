class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        lines = []
        for st, en in intervals:
            lines.append((st, -1))
            lines.append((en, 1))

        lines.sort()

        ans = []
        num_events = 0
        curr_start, curr_end = -1, -1

        for event, kind in lines:
            prev_num_events = num_events
            num_events -= kind

            if prev_num_events == 0 and num_events == 1:
                curr_start = event
            if num_events == 0:
                curr_end = event
                ans.append((curr_start, curr_end))

        return ans