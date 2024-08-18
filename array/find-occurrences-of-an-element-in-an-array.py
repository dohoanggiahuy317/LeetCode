class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        temp = []
        for i in range(len(nums)):
            if nums[i] == x:
                temp.append(i)
                
        ans = []
        
        
        for t in queries:
            if t - 1 >= len(temp):
                ans.append(-1)
            else:
                ans.append(temp[t - 1])
                
        return ans
                