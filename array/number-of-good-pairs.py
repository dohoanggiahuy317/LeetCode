class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        ans = 0

        for num in nums:
            ans += freq[num]
            freq[num] += 1
        
        return ans