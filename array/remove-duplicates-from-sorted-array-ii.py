class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = nums[0]
        count = 0

        for i in range(1, len(nums)):
            if nums[i] == s and count >= 1:
                count += 1
                nums[i] = -101
            elif nums[i] == s and count == 0:
                count += 1
            else:
                count = 0
                s = nums[i]

        curr = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] != -101:
                count += 1
                temp = nums[i]
                nums[i] = -101
                nums[curr] = temp
                curr += 1

        return count

        