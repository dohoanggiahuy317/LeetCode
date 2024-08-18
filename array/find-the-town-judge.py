class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d = {}

        for i in range(1, n+1):
            d[i] = {
                "t": set(),
                "f": set()
            }

        for a, b in trust:
            d[a]["t"].add(b)
            d[b]["f"].add(a)

        for x, y in d.items():
            if len(y["t"]) == 0 and len(y["f"]) == n-1:
                return x

        return -1