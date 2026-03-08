class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        direct_to = defaultdict(lambda: False)

        for u, v in paths:
            direct_to[u] = True
            direct_to[v]

        for city, b in direct_to.items():
            if b == False:
                return city