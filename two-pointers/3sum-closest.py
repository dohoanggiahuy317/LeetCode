class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        curr = 10**6
        ans = 0

        for i in range(len(nums)-2):
            s = i + 1
            l = len(nums) - 1

            while s < l:
                if abs(target - nums[i] - nums[s] - nums[l]) < curr:
                    ans = [nums[i], nums[s], nums[l]]
                    curr = abs(target - nums[i] - nums[s] - nums[l])
                    ans = nums[i] + nums[s] + nums[l]
                    # print(nums[i], nums[s], nums[l])

                if nums[i] + nums[s] + nums[l] > target:
                    l -= 1
                else:
                    s += 1

        return ans