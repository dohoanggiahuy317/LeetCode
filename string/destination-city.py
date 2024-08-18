class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        in_li = set(map(lambda x: x[0], paths))

        for i in paths:
            if i[1] not in in_li:
                return i[1]
