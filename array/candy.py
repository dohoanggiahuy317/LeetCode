class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        flow_tracker = [0]
        curr_min = 0
        total = 0

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                flow_tracker.append(flow_tracker[-1] + 1)
            else:
                flow_tracker.append(flow_tracker[-1] - 1)
                curr_min = min(curr_min, flow_tracker[-1])
            total += flow_tracker[-1]

        # print(total, curr_min, flow_tracker)

        ans = max(0, (1 - curr_min)) * len(ratings) + total
        return ans