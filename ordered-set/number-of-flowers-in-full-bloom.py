class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        tracker = defaultdict(int)

        for start, end in flowers:
            tracker[start] += 1
            tracker[end + 1] -= 1

        days = sorted(tracker.keys())
        ans = [0] * len(people)
        sorted_people = sorted([(person, i) for i, person in enumerate(people)])
        
        day_ptr = 0
        num_flower = 0
        for person, i in sorted_people:
            while day_ptr < len(days) and days[day_ptr] <= person:
                num_flower += tracker[ days[day_ptr] ]
                day_ptr += 1
                
            ans[i] = num_flower
                
        return ans