class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        
        ans = 0

        while True:
            if nums == sorted(nums) or len(nums) <= 1:
                return ans

            curr_ind = -1
            curr_sum = float("INF")

            for i in range(len(nums)-1):
                if nums[i] + nums[i+1] < curr_sum:
                    curr_ind = i
                    curr_sum = nums[i] + nums[i+1]

            nums[curr_ind] = curr_sum
            nums.pop(curr_ind + 1)
            # print(nums)
            ans += 1

        return ans