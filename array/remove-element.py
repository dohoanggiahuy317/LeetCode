class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums == []:
            return

        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 101
        
        nums.sort()
        while len(nums) > 0 and nums[-1] == 101:
            nums.pop(-1)
        
        # return count
        