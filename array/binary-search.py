class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if len(nums) == 1:
        #     return 0 if nums[0] == target else -1
        
        l, r = 0, len(nums) - 1
       
        while l <= r:
            m = (l + r) // 2
            # print(l, r, m)
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        
        return -1