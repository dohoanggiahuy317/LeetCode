class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        curr, count = 0, 0
        pref = defaultdict(int, {0: 1})

        for num in nums:
            curr += num % 2
            pref[curr] += 1
            count += pref[curr - k]
            
        return count



            