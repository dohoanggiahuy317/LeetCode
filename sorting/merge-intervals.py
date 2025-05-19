class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []
        curr_int = intervals.pop(0)

        while intervals:
            next_int = intervals.pop(0)

            if next_int[0] <= curr_int[1]:
                curr_int[1] = max(curr_int[1], next_int[1])
            else:
                ans.append(curr_int)
                curr_int = next_int

        ans.append(curr_int)

        return ans
