class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        
        ans = []

        for i in range(len(nums)):
            ans.append(nums[i])
            for j in range(i):
                if 0 < nums[j] - nums[i] <= limit:
                    ans[i], ans[j] = ans[j], ans[i]
                    break
        
        return ans