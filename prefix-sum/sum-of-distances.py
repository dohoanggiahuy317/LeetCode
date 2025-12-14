from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        total_count = defaultdict(int)
        total_sum = defaultdict(int)

        for i, v in enumerate(nums):
            total_count[v] += 1
            total_sum[v] += i

        left_count = defaultdict(int)
        left_sum = defaultdict(int)

        ans = [0] * len(nums)

        for i, v in enumerate(nums):
            total_count[v] -= 1
            total_sum[v] -= i

            left_dist = i * left_count[v] - left_sum[v]
            right_dist = total_sum[v] - i * total_count[v]

            ans[i] = left_dist + right_dist

            left_count[v] += 1
            left_sum[v] += i

        return ans