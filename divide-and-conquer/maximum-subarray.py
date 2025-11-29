class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pref_sum = list(accumulate(nums))
        pref_min = []

        for i, s in enumerate(pref_sum):
            pref_min.append(s if i == 0 else min(s, pref_min[-1]))
        
        ans = 0
        for i, s in enumerate(pref_sum):
            ans = max(ans, max(s, s - pref_min[i]))
        
        return ans