class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref_prod_left = [1] * n
        curr = 1
        for i, num in enumerate(nums):
            pref_prod_left[i] = curr * num
            curr = pref_prod_left[i]

        pref_prod_right = [1] * n
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            pref_prod_right[i] = curr * nums[i]
            curr = pref_prod_right[i]

        ans = []

        for i in range(len(nums)):
            left = pref_prod_left[i - 1] if i > 0 else 1
            right = pref_prod_right[i + 1] if i < len(nums) - 1 else 1
            ans.append(left * right)

        return ans