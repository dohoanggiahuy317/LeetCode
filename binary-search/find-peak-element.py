class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-inf] + nums + [-inf]
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r) // 2

            if nums[m - 1] < nums[m] > nums[m + 1]:
                return m - 1

            if nums[m - 1] > nums[m] > nums[m + 1]:
                r = m - 1
            elif nums[m-1] < nums[m] < nums[m + 1]:
                l = m + 1
            else:
                if nums[m] < nums[r]:
                    l = m+1
                else:
                    r = m-1
        
        return l - 1