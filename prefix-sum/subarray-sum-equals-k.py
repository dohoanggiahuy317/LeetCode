from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            if nums[0] == k:
                return 1
            return 0

        n = len(nums)
        pref_sum = [0] * (n+1)
        freq = Counter()

        # loop through the nums arr
        for i in range(n):
            pref_sum[i+1] = pref_sum[i] + nums[i]
            freq[pref_sum[i+1]] += 1

        ans = 0
        for s in pref_sum:
            if s + k in freq:
                ans += freq[s+k]

        return ans