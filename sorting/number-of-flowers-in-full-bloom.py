class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        MAX_DAY = max([day[1] for day in flowers])
        tracker = [0] * (MAX_DAY + 2)

        for start, end in flowers:
            tracker[start] += 1
            tracker[end + 1] -= 1

        prefix_tracker = list(accumulate(tracker))
        # print(prefix_tracker)
        ans = []
        for person in people:
            if 0 <= person <= MAX_DAY + 1:
                ans.append(prefix_tracker[person])
            else:
                ans.append(0)
        return ans