from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d = Counter(answers)

        ans = 0
        for u, v in d.items():
            if u == 0:
                ans += v
            else:
                ans += u + 1

        return ans