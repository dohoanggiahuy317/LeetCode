class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pref_sum = 0
        sum_nums = sum(nums)

        for i, num in enumerate(nums):
            suff_sum = sum_nums - pref_sum - num
            if suff_sum == pref_sum:
                return i
            pref_sum += num

        return -1