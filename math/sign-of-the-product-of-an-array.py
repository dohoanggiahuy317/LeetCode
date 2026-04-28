class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1

        for num in nums:
            if num == 0:
                return 0
            ans *= num // abs(num)

        return ans