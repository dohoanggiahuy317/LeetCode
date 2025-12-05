class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        DESTROY = -1
        BLOOM = 1
        VISIT = 0

        lines = defaultdict(int)

        for s, e in flowers:
            lines[s] += BLOOM
            lines[e + 1] += DESTROY

        for person in people:
            lines[person] += VISIT

        blooms = defaultdict()
        num = 0
        for t in sorted(lines.keys()):
            num += lines[t]
            blooms[t] = num

        return [blooms[person] for person in people]