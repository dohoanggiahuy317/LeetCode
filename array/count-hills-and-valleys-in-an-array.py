class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        i = 0
        while i < len(nums):
            num = nums[i]
            pad_left = 1
            while i - pad_left >= 0 and nums[i - pad_left] == num:
                pad_left += 1

            pad_right = 1
            while i + pad_right < len(nums) and nums[i + pad_right] == num:
                pad_right += 1

            if i - pad_left >= 0 and i + pad_right < len(nums):
                if (nums[i-pad_left] < num > nums[i+pad_right]) or (nums[i-pad_left] > num < nums[i+pad_right]):
                    ans += 1
                    i += pad_right
                    continue

            i += 1

        return ans
            
