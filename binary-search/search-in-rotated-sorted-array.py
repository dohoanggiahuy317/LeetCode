class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) >> 1

            if target == nums[m]:
                return m

            if nums[l] <= nums[m]:
                if target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1

        return -1

