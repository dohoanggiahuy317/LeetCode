from collections import Counter

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        half_n = n // 2
        diffs = []

        for i in range(half_n):
            diffs.append(abs(nums[i] - nums[n - i - 1]))
        
        freq = Counter(diffs)

        s = set()
        temp = {}

        for u, v in freq.items():
            if v not in temp:
                temp[v] = u
            else:
                temp[v] = min(u, temp[v])
        
        if len(freq) == 1:
            return 0

        min_changes = float('inf')

        for u, best_diff in temp.items():
            changes = 0
            for i in range(half_n):
                current_diff = abs(nums[i] - nums[n - i - 1])
                if current_diff != best_diff:
                    if nums[i] + best_diff > k and nums[i] - best_diff < 0 and nums[n - i - 1] + best_diff > k and nums[n - i - 1] - best_diff < 0:
                        changes += 2
                    else:
                        changes += 1
            min_changes = min(min_changes, changes)
        
        return min_changes