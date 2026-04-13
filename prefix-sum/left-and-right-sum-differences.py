class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        curr_left, curr_right = 0, sum(nums)
        ans = []

        for i, num in enumerate(nums):
            curr_right -= num
            ans.append(abs(curr_left - curr_right))
            curr_left += num

        return ans