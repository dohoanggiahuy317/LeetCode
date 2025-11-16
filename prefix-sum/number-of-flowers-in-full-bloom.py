class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        tracker = defaultdict(int)

        for start, end in flowers:
            tracker[start] += 1
            tracker[end + 1] -= 1

        prefix_tracker = []
        MIN_DAY = inf
        MAX_DAY = -inf
        for day in sorted(tracker.keys()):
            freq = tracker[day] + (prefix_tracker[-1][1] if prefix_tracker else 0)
            prefix_tracker.append((day, freq))
            MIN_DAY = min(MIN_DAY, day)
            MAX_DAY = max(MAX_DAY, day)
        
        ans = []
        for person in people:
            if not (MIN_DAY <= person <= MAX_DAY):
                ans.append(0)
            else:
                l, r = 0, len(prefix_tracker) - 1
                temp = -1
                while l <= r:
                    m = (l + r) // 2
                    if person >= prefix_tracker[m][0]:
                        temp = m
                        l = m + 1
                    else:
                        r = m - 1

                ans.append(prefix_tracker[temp][1])
                
        return ans