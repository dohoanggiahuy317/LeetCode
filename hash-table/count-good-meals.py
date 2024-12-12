from collections import Counter
import math

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        if len(deliciousness) == 1:
            if math.log(deliciousness[-1]) - int(math.log(deliciousness[-1])) == 0:
                return 1
            return 0

        freq = Counter()
        for deli in deliciousness:
            freq[deli] += 1

        deliciousness.sort()
        max_base = int(math.log(deliciousness[-1] + deliciousness[-2], 2))
        ans = 0

        # print(max_base, freq)

        for i in range(max_base + 1):
            curr_sum = 2 ** i
            
            for k, v in freq.items():
                target = curr_sum - k
                if target in freq:
                    if target == k:
                        ans += v * (v-1) //2
                    else:
                        ans += v * freq[target] / 2

        return int(ans)
        