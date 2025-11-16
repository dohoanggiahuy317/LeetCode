class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        MAX_DAY = max([day[1] for day in flowers])
        tracker = [0] * (MAX_DAY + 2)

        for start, end in flowers:
            tracker[start] += 1
            tracker[end + 1] -= 1

        prefix_tracker = list(accumulate(tracker))
        # print(prefix_tracker)
        return [prefix_tracker[person] for person in people]