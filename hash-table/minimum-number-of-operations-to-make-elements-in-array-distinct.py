from collections import Counter
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        d = Counter(nums)

        ans = 0
        while max(list(d.values())) > 1 and nums:
            if len(nums) >= 3:
                for _ in range(3):
                    ele = nums.pop(0)
                    d[ele] -= 1
            else:
                nums = []
            ans += 1

        
        return ans