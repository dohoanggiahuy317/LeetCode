class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        triplet = []

        for i, num in enumerate(nums):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            
            target_used = {nums[k]: False for k in range(i + 1, n)}
            target_count = Counter(nums[i + 1:])

            for j in range(i + 1, n):
                target = - nums[i] - nums[j]

                if target not in target_used:
                    continue
                if target_used[target]:
                    continue
                if nums[j] == target and target_count[target] == 1:
                    continue

                triplet.append([nums[i], target, nums[j]])
                target_used[target] = True
                target_used[nums[j]] = True

        return triplet

