class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_other = [0] * (n + 1)
        other_trust = [0] * (n + 1)

        for a, b in trust:
            trust_other[a] += 1
            other_trust[b] += 1

        for i in range(1, n + 1):
            if trust_other[i] != 0:
                continue
            if other_trust[i] != n - 1:
                continue

            return i

        return -1

        