class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_max = [height[0]] * n
        suffix_max = [height[-1]] * n

        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], height[i])

        ans = 0
        for i in range(n):
            ans += min(suffix_max[i], prefix_max[i]) - height[i]

        return ans
