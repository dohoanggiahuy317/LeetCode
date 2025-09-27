class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        sorted_intervals = SortedList(intervals)

        idx = 1
        ans = 0
        while idx < len(sorted_intervals):
            start, end = sorted_intervals[idx]
            if start < sorted_intervals[idx - 1][1]:
                sorted_intervals.pop(idx)
                ans += 1
            else:
                idx += 1
        
        return ans