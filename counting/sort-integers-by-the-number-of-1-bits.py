class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        n = list(map(lambda x: [x, sum( list(map(int, list(bin(x)[2:]))))], arr))

        n.sort(key=lambda x: (x[1], x[0]))

        ans = list(map(lambda x: x[0], n))

        return ans
        