from collections import Counter

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2 == 1:
            return False

        d = Counter(nums)
        nums = []
        for u, v in d.items():
            if v % 2 == 1:
                nums.append(u)
        if len(nums) == 0:
            return True
        

        target = s // 2
        nums.sort()

        def addup(curr, i):
            nonlocal ans, nums

            if curr == target:
                ans = True
                return

            if curr > target:
                return

            if i >= len(nums):
                return

            addup(curr + nums[i], i + 1)
            addup(curr, i + 1)
        
        ans = False
        addup(0, 0)
        return ans