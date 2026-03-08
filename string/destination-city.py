class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        connection = defaultdict(int)
        cities = set()

        for u, v in paths:
            connection[u] += 1
            cities.add(u)
            cities.add(v)

        for city in cities:
            if connection[city] == 0:
                return city