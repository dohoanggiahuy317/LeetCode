class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        
        if len(set(nums[:k])) >= m:
            curr_sum = sum(nums[:k])
        else:
            curr_sum = 0
        ans = curr_sum
        
        
        for s in range(1, len(nums) + 1 - k):
            sub_li = set(nums[s: s + k])
            
            if curr_sum == 0:
                curr_sum = sum(nums[s: s + k])
            else:
                curr_sum = curr_sum + nums[s+k-1] - nums[s-1]
            
            if len(sub_li) >= m:
                ans = max(ans, curr_sum)
                
        # print(curr_sum)
                
        return ans
            
            
            
            
            
            
            
            