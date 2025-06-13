class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = -float("INF")
        freq = defaultdict(lambda: inf)
        pref = 0
        for num in nums:
            pref += num
            if num - k in freq:
                ans = max(ans, pref - freq[num-k] + num-k)
            if k + num in freq:
                ans = max(ans, pref - freq[k+num] + k+num)
            freq[num] = min(freq[num], pref)

        return ans if ans != -float("INF") else 0