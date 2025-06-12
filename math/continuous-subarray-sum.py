class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        freq = defaultdict(int, {0:0})
        pref = 0
        for num in nums:
            pref = (pref + num) % k
            if (pref - k) % k in freq:
                return True
        
        return False
            