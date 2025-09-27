class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        sorted_intervals = sorted(intervals, key = lambda x: (x[1], x[0]))
        # print(sorted_intervals)

        prev, curr = 0, 1
        ans = 0
        while curr < len(sorted_intervals):
            start, _ = sorted_intervals[curr]
            if start < sorted_intervals[prev][1]:
                ans += 1
            else:
                prev = curr
            curr += 1
            # print(idx, sorted_intervals)
        
        return ans