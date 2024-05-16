class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        d = Counter()

        for x, y in rectangles:
            d[x/y] += 1
        
        ans = 0
        for u, v in d.items():
            ans += v * (v-1) // 2

        return ans