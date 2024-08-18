class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 51
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                ans = 0
                for x in range(i, j+1):
                    # print(x)
                    ans = ans | nums[x]
                    
                if ans >= k:
                    res = min(res, j - i + 1)
        
        if res == 51:
            return -1
        return res