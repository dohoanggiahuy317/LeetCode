class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pref_prod = defaultdict(lambda : 1)
        for i, num in enumerate(nums):
            pref_prod[i] = pref_prod[i - 1] * num

        ans = [1] * n
        suff_prod = 1
        for i in range(n - 1, -1, -1):
            ans[i] = suff_prod * pref_prod[i - 1]
            suff_prod *= nums[i]

        return ans