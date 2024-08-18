class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        def countPairs(range_dist):
            nonlocal nums

            count = 0
            left = 0

            for right in range(1, len(nums)):
                while nums[right] - nums[left] > range_dist:
                    left += 1
                count += right - left

            return count
        
        
        nums.sort()

        min_dist = 0
        max_dist = nums[-1] - nums[0]

        while min_dist < max_dist:
            mid_dist = (max_dist + min_dist) // 2
            pair_count = countPairs(mid_dist)

            if pair_count < k:
                min_dist = mid_dist + 1
            else:
                max_dist = mid_dist

        return min_dist