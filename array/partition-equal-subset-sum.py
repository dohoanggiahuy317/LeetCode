from collections import Counter

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2 == 1:
            return False

        target = s // 2
        nums.sort()


        def addup(curr, tu, i):
            nonlocal ans, nums, visited

            if curr == target:
                ans = True
                return

            if curr > target:
                return

            if i >= len(nums):
                return
            
            if tu in visited:
                return

            visited.add(tu)

            addup(curr + nums[i], tuple(list(tu) + [nums[i]]), i + 1)
            addup(curr, tu, i + 1)
        
        ans = False
        visited = set()
        addup(0, tuple(), 0)
        return ans