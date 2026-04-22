class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        curr, count = 0, 0
        pref = defaultdict(int, {0: 1})

        for num in nums:
            curr += num
            count += pref[curr - goal]
            pref[curr] += 1

        return count
