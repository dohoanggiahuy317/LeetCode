class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pref_sum = list(accumulate(nums))
        suff_sum = list(accumulate(nums[::-1]))[::-1]
        sum_nums = sum(nums)

        for i, num in enumerate(nums):
            p, s = 0, sum_nums
            if i != 0:
                p = pref_sum[i - 1]
            if i != len(nums) - 1:
                s = suff_sum[i + 1]

            if p == s:
                return i

        return -1