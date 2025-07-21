class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref_right = [1] * n

        for i in range(n-1, 0, -1):
            pref_right[i-1] = pref_right[i] * nums[i]
        
        pref_left = 1
        ans = []
        for i, num in enumerate(nums):
            ans.append(pref_right[i] * pref_left)
            pref_left *= num
        
        return ans