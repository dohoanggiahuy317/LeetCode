class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        smallest_group = list(accumulate(nums[:k]))
        
        curr = sum(nums[:k])
        smallest_group[k - 1] = min(smallest_group[k - 1], curr)
        ans = curr

        for r in range(k, len(nums)):
            l = r - k + 1

            curr += nums[r]
            if r % k == k - 1:
                ans = max(ans, curr)
            ans = max(ans, curr - smallest_group[r % k])

            smallest_group[r % k] = min(smallest_group[r % k], curr)

        return ans

            



