class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        best_diff = inf
        best_idx = -1

        pref_sum = list(accumulate(nums))
        total = pref_sum [-1]

        for i, (pref, num) in enumerate(zip(pref_sum, nums)):
            suff = total - pref
            diff = abs(
                        pref//(i + 1) - 
                        (suff//(n - i - 1) if i < n - 1 else 0)
                        )

            if diff < best_diff:
                best_diff = diff
                best_idx = i
            
        return best_idx
