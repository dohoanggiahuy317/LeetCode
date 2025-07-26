class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        pivot = 0

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[m] > nums[r]:
                if nums[m] > target and nums[r] < target:
                    r = m - 1
                else:
                    l = m + 1
            
            else:
                if nums[m] < target and nums[r] > target:
                    l = m + 1
                else:
                    r = m - 1
            
        return -1

