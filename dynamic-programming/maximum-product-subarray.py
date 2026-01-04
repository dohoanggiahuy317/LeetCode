class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans1 = nums[0]
        ans2 = nums[len(nums) - 1]

        curr1 = curr2 = 1

        for l in range(len(nums)):
            # print(ans1, ans2)
            curr1 *= nums[l]
            ans1 = max(ans1, curr1)

            if curr1 == 0:
                curr1 = 1

            curr2 *= nums[len(nums)-1 - l]
            ans2 = max(ans2, curr2)

            if curr2 == 0:
                curr2 = 1

        return max(ans1, ans2)