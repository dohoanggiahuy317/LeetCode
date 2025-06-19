class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nnums = sorted(nums)
        ans, curr = 0, nnums[0]
        for num in nnums:
            if num - curr > k:
                ans += 1
                curr = num

        return ans + 1