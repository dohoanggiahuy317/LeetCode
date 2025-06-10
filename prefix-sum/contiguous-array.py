class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        freq = defaultdict(lambda: inf, {0:-1})
        pref, ans = 0, 0

        for j, num in enumerate(nums):
            pref += 1 if num == 1 else -1
            ans = max(ans, j - freq[pref])
            freq[pref] = min(j, freq[pref])

        return ans