class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        num2pos = {num: i for i, num in enumerate(nums)}

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                target = - nums[i] - nums[j]

                if target in num2pos and num2pos[target] > j:
                    ans.add(tuple(sorted([nums[i], nums[j], target])))

        return [list(sub) for sub in ans]
