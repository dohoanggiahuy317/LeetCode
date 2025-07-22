class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        visited, curr, ans = set(), 0, 0
        l = 0
        for num in nums:
            while num in visited:
                visited.remove(nums[l])
                curr -= nums[l]
                l += 1
            
            visited.add(num)
            curr += num
            ans = max(ans, curr)

        return ans