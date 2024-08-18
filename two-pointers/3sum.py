class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        nums.sort()

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]

            while l < r:
                if nums[l] + nums[r] == target:
                    ans.add((nums[l], nums[r], -target))
                    l += 1
                    r -= 1

                elif nums[l] + nums[r] < target:
                    l += 1
                
                elif nums[l] + nums[r] > target:
                    r -= 1

        rans = []

        for x in ans:
            rans.append(list(x))

        return rans
        