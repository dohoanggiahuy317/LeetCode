class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        p = 0
        while l < r:
            m = (l + r) // 2
            p = m
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        p = l
        nnums = nums[p:] + nums[:p]
        # print(nums)
        l, r = 0, len(nnums) - 1
        while l <= r:
            m = (l + r) // 2
            if nnums[m] < target:
                l = m + 1
            elif nnums[m] > target:
                r = m - 1
            else:
                return (m + p) % len(nnums)

        return -1
