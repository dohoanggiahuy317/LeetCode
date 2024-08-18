class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        n = [str(x) for x in range(1, n+1)]

        n.sort()

        return list(map(int, n))