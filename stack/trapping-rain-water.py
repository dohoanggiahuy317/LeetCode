class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_max = [height[0]] * n
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], height[i])

        suffix_max = height[-1]
        ans = 0
        for i in range(n - 1, -1, -1):
            suffix_max = max(suffix_max, height[i])
            ans += min(suffix_max, prefix_max[i]) - height[i]

        return ans
            