class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        pref_sum = list(accumulate(nums))
        total = pref_sum[-1]
        count = 0

        for pref in pref_sum[:-1]:
            count += int(pref >= total - pref)

        return count