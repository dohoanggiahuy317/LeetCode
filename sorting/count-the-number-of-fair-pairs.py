from bisect import bisect, bisect_left
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return sum(
            bisect(nums, upper - num, hi=i) - bisect_left(nums, lower - num, hi=i)
            for i, num in enumerate(nums)
        )