class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        if len(nums) < 4:
            return []
        nums.sort()

        ans = set()
        for x1 in range(len(nums) - 3):
            for x2 in range(x1 + 1, len(nums) - 2):
                l = x2 + 1
                r = len(nums) - 1
                loc_target = target - nums[x1] - nums[x2]

                while l < r:
                    if nums[l] + nums[r] == loc_target:
                        ans.add( tuple(sorted([nums[x1], nums[x2], nums[l], nums[r]]) ))
                        l += 1
                        r -= 1

                    elif nums[l] + nums[r] < loc_target:
                        l += 1
                    
                    elif nums[l] + nums[r] > loc_target:
                        r -= 1 


        rans = []

        for x in ans:
            rans.append(list(x))


        return rans