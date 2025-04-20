from collections import Counter
from math import ceil

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d = Counter(answers)

        ans = 0
        for u, v in d.items():
            if u == 0:
                ans += v
            else:
                ans += ceil(v/(u + 1)) * (u+1)

        return ans