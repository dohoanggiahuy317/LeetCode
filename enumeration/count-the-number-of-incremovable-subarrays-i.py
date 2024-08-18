class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        count = 0
        
        for l in range(1, len(nums)):
            for i in range(len(nums) - l + 1):
                new_li = nums[:i] + nums[i+l:]
                # print(new_li)
                bo = True
                
                if len(new_li) > 1:
                    for t in range(len(new_li) - 1):
                        if new_li[t] >= new_li[t + 1]:
                            bo = False
                            break
                            
                # print(bo)
                
                if bo:
                    count += 1
                
                
        return count + 1