class Solution:
    #revere(120) =21 
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        seen = {}
        ans = inf
        
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            
            rev_num = int(str(num)[::-1])

            if rev_num in seen:
                j = seen[rev_num]
                ans = min(ans, j - i)
            
            seen[num] = i
                                  
        return ans if ans != inf else -1