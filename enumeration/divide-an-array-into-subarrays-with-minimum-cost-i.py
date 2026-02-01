class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min1, min2 = inf, inf

        for num in nums[1:]:
            if num < min2:
                min2 = num
            
            if min1 > min2:
                min1, min2 = min2, min1

        return nums[0] + min1 + min2