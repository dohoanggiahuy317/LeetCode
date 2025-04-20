from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d = Counter(answers)

        ans = 0
        for u, _ in d.items():
            ans += u + 1

        return ans