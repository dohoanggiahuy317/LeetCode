from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        f = [[0]*(k+1) for _ in range(len(nums))]
        ans = 1
        for i in range(len(nums)):
            f[i][0] = 1
            for j in range(k+1):
                for l in range(i):
                    if nums[l] == nums[i]:
                        f[i][j] = max(f[i][j], f[l][j]+1)
                    if j > 0:
                        f[i][j] = max(f[i][j], f[l][j-1]+1)
                ans = max(ans, f[i][j])
        return ans