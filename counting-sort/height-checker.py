class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expect = sorted(heights)
        ans = 0

        for i in range(len(heights)):
            if expect[i] != heights[i]:
                ans += 1

        return ans