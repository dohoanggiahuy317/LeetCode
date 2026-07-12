class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = 2 ** (len(nums) + 1) - 1

        for i, num in enumerate(nums):
            if num != i:
                ans = ans & i

        return ans if ans != 2 ** (len(nums) + 1) - 1 else 0