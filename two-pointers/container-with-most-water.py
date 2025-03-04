class Solution:
    def maxArea(self, height: List[int]) -> int:

        sort_height = []
        for i in range(1, len(height) + 1):
            sort_height.append((i, height[i-1]))
        
        sort_height = sorted(sort_height, key=lambda x: x[1], reverse=True)
        maxx, maxy = sort_height.pop(0)

        lx, ly = maxx, maxy
        rx, ry = maxx, maxy

        ans = 0

        while sort_height:
            curx, cury = sort_height.pop(0)

            if curx < lx:
                ans = max(ans, (rx - curx) * cury )
                lx = curx
                ly = cury
            elif curx > rx:
                ans = max(ans, (curx - lx) * cury )
                rx = curx
                ry = cury

        return ans