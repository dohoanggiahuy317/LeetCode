class Solution:
    def maxArea(self, height: List[int]) -> int:
        s = 0
        e = len(height) - 1

        curr = min(height[s], height[e]) * (e - s)

        while s < e:
            if height[s] < height[e]:
                s += 1
            elif height[e] < height[s]:
                e -= 1
            elif height[s] == height[e]:
                s += 1
                # e -= 1

            # print(s, e, min(height[s], height[e]) * (e - s))

            curr = max(curr, min(height[s], height[e]) * (e - s))

        return curr