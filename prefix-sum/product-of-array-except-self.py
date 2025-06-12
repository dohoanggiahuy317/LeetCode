class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefL = [1] * (n+1)

        for i, num in enumerate(nums):
            prefL[i+1] = prefL[i] * num

        ans = [1] * n
        prefR = 1
        for i in range(n-1, -1, -1):
            ans[i] = prefR * prefL[i]
            prefR *= nums[i]

        return ans