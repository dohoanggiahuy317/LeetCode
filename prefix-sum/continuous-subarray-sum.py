class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        freq = defaultdict(lambda: inf, {0:-1})
        pref = 0

        for i, num in enumerate(nums):
            pref = (pref + num) % k
            if pref in freq and i - freq[pref] > 1:
                return True
            freq[pref] = min(freq[pref], i)
        
        return False
            