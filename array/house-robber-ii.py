class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return max(nums)

        memoir1 = [0] * n
        memoir2 = [0] * n

        memoir1[0] = nums[0]
        memoir1[1] = nums[1]
        memoir1[2] = nums[0] + nums[2]

        for i in range(3, n - 1):
            memoir1[i] = max(memoir1[i - 2], memoir1[i - 3]) + nums[i]

        memoir2[0] = 0
        memoir2[1] = nums[1]
        memoir2[2] = nums[2]
        memoir2[3] = nums[1] + nums[3]

        for i in range(4, n):
            memoir2[i] = max(memoir2[i - 2], memoir2[i - 3]) + nums[i]

        
        return max(max(memoir1), max(memoir2))