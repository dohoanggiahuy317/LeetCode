class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        nums.sort()

        counter = 0
        curr_sum = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                counter += 1
                curr_sum += counter
            else:
                curr_sum += counter

        return curr_sum

1
3
6
10
15