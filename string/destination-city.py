class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        connection = defaultdict(lambda: False)
        cities = set()

        for u, v in paths:
            connection[u] = True
            cities.add(u)
            cities.add(v)

        for city in cities:
            if connection[city] == False:
                return city