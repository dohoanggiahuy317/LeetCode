class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        temp = [-1]
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                temp.append(i)
        temp.append(len(nums) - 1)
                
        ans = 0
        
        for x in range(1, len(temp)):
            c = temp[x] - temp[x - 1]
            
            ans += c * (c + 1) // 2
            
        return ans