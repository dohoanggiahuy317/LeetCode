class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left_pref = [nums[0]] * len(nums)
        right_pref = [nums[-1]] * len(nums)

        for i in range(1, len(nums)):
            left_pref[i] = left_pref[i-1] * nums[i]
            right_pref[-i-1] = right_pref[-i] * nums[-i-1]
        left_pref = [1] + left_pref + [1]
        right_pref = [1] + right_pref + [1]

        return [left_pref[i-1] * right_pref[i+1] for i in range(1, len(nums)+1)]