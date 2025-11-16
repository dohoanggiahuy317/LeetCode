class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        line = defaultdict(int)

        for start, end in flowers:
            line[start] += 1
            line[end + 1] -= 1
        
        for person in people:
            line[person] += 0

        count = defaultdict(int)
        num_flow = 0
        for day in sorted(line.keys()):
            num_flow += line[day]
            count[day] = num_flow
                
        return [count[person] for person in people]