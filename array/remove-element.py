class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        
        while i < len(nums):
            num = nums[i]
            if num != val:
                k += 1
                i += 1
            else:
                nums.pop(i)

        # print(nums)
        return k