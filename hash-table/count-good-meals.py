from collections import Counter
import math

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        if len(deliciousness) == 1:
            if math.log(deliciousness[-1]).isdigit():
                return 1
            return 0

        return 0

        # freq = Counter()
        # for deli in deliciousness:
        #     freq[deli] += 1

        # deliciousness.sort()
        # max_base = int(Math.log(deliciousness[-1] + ))
        