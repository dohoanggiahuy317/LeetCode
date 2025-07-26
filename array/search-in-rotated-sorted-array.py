class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        pivot = 0

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[m] >= nums[l]:
                if nums[m] > target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

            # print(m, l, r)
            
        return -1

