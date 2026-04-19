class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pref_sum = list(accumulate(nums))
        remainder = defaultdict(int, {0: -1})

        for i, pref in enumerate(pref_sum):
            rem = pref % k
            if rem in remainder:
                if i > remainder[rem] + 1:
                    return True
            else:
                remainder[rem] = i
                
        return False