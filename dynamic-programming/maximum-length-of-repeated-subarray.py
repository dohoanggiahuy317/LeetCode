class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * n for _ in range(m)]

        ans = 0
        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + (dp[i - 1][j - 1] if i > 0 and j > 0 else 0)
                    ans = max(ans, dp[i][j])

        return ans