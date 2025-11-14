from typing import List
from sortedcontainers import SortedList

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        freq_prefix = [0] * n
        for i, num in enumerate(nums):
            if i == 0:
                freq_prefix[i] = 1 if num == target else 0
            else:
                freq_prefix[i] = freq_prefix[i-1] + (1 if num == target else 0)

        ans = 0
        diffs = SortedList()
        diffs.add(-1)

        for i in range(n):
            curr_diff = i - 2 * freq_prefix[i]

            idx = bisect.bisect_right(diffs, curr_diff)
            ans += len(diffs) - idx

            diffs.add(curr_diff)

        return ans