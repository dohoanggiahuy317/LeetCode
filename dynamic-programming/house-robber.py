class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        x_3 = nums[-1]
        x_2 = nums[-2]
        x_1 = nums[-3] + nums[-1]


        for i in range(len(nums) - 4, -1, -1):
            temp = nums[i] + max(x_2, x_3)
            x_3, x_2, x_1 = x_2, x_1, temp
        
        return max(x_1, x_2, x_3)