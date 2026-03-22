class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        best_dist = inf
        best_sum = -1
        nums.sort()

        for i, num in enumerate(nums):
            j, k = i + 1, n - 1

            while j < k:
                dist = abs(nums[i] + nums[j] + nums[k] - target)
                if dist < best_dist:
                    best_dist = dist
                    best_sum = nums[i] + nums[j] + nums[k]
                
                if nums[i] + nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
        
        return best_sum
                    

        