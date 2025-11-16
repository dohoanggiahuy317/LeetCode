from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = sorted(f[0] for f in flowers)
        ends = sorted(f[1] for f in flowers)

        ans = []
        for person in people:
            this_start = bisect.bisect_right(starts, person)
            this_end = bisect.bisect_left(ends, person)
            ans.append(this_start - this_end)

        return res