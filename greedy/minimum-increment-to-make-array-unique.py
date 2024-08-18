class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:        
        nums.sort()
        d = Counter(nums)
        ans = 0
        last = 0

        for u, v in d.items():
            ans += (0 + v-1) * v // 2  + max(last - u, 0) * v
            last = max(last, u) + v

        return ans