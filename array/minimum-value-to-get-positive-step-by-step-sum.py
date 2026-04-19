class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pref_sum = list(accumulate(nums))
        return max(-min(pref_sum) + 1, 1)