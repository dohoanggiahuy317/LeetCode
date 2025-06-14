class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, c = 0, 0
        ans = 0

        for right, num in enumerate(nums):
            if num == 0:
                c += 1
                while c > k:
                    if nums[left] == 0:
                        c -= 1
                    left += 1
            
            ans = max(ans, right - left + 1)

        return ans 
                