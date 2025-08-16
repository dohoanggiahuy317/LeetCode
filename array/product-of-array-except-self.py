class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefL = [1] * n
        for i, num in enumerate(nums):
            prefL[i] = num * (prefL[i - 1] if i > 0 else 1)

        ans = [1] * n
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = curr * (prefL[i - 1] if i > 0 else 1)
            curr *= nums[i]

        return ans