class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        t = [(a**2 + b**2, a * b) for a, b in dimensions]
        t.sort(reverse = True)
        return t[0][1]