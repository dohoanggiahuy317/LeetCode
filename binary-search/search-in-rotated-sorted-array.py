class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        p = 0
        while l <= r:
            m = (l + r) // 2
            print(l, r, m)
            if nums[m] > nums[l]:
                if nums[m+1] < nums[m]:
                    p = m+1
                    break
                l = m + 1
            elif nums[m] < nums[l]:
                if nums[m-1] > nums[m]:
                    p = m
                    break
                r = m - 1
            else:
                p = m
                break
            
        nnums = nums[p:] + nums[:p]
        l, r = 0, len(nnums) - 1
        while l <= r:
            m = (l + r) // 2
            if nnums[m] < target:
                l = m + 1
            elif nnums[m] > target:
                r = m - 1
            else:
                return m + p

        return -1
