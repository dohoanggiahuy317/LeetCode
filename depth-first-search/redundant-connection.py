class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = set()

        for x, y in edges:
            if x in visited and y in visited:
                return [x, y]

            visited.add(x)
            visited.add(y)