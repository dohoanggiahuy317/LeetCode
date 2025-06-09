class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int, {0:1})
        pref = 0
        ans = 0
        for num in nums:
            pref = pref + num
            ans += freq[pref % k]
            freq[pref%k] += 1
        return ans