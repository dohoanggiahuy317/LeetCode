class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        l = 0
        curr_prod = 1
        ans = 0

        for r, num in enumerate(nums):
            curr_prod *= num

            while l <= r and curr_prod >= k:
                curr_prod //= nums[l]
                l += 1
            
            ans += (r - l + 1)

        return ans