class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        li = sorted(list(map(lambda x: x[0], points)))

        ans = 0

        for i in range(len(li) - 1):
            ans = max(ans, li[i+1] - li[i])

        return ans