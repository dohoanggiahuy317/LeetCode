class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        pref_max = [-inf] * n
        suff_min = [inf] * n

        for i, num in enumerate(nums):
            pref_max[i] = max(num, pref_max[i - 1] if i > 0 else -inf)
        
        for i in range(n - 1, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1] if i < n - 1 else inf) 

        for i in range(n):
            if pref_max[i] - suff_min[i] <= k:
                return i

        return -1
