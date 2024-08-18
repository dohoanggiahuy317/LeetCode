class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [1 for _ in range(n)]    

        left = [1 for _ in range(n)]
        right = [1 for _ in range(n)]

        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]

            right[n-1 - i] = right[n - i] * nums[n - i]


        for i in range(n):
            ans[i] = left[i] * right[i]


        return ans

