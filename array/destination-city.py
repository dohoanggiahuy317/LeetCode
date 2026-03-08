class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        direct_to = defaultdict(lambda: False)
        cities = set()

        for u, v in paths:
            direct_to[u] = True
            direct_to[v]

        for city in cities:
            if direct_to[city] == False:
                return city