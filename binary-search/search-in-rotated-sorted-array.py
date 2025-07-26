class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        pivot = -1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[l]:
                l = m
            else:
                pivot = m
                r = m - 1

        l, r = 0, pivot
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

                l, r = 0, pivot
        l, r = pivot, len(nums) - 1
        ans = 0
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return -1

        
