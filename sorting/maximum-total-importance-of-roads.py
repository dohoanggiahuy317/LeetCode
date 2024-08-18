class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        d = Counter()

        for u, v in roads:
            d[u] += 1
            d[v] += 1

        start = n
        ans = 0
        for u in sorted(list(d.values()), reverse = True):
            ans += u * start
            start -= 1

        return ans