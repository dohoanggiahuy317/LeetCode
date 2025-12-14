class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        nums = nums + nums
        stack = []
        ans = [-1] * len(nums)

        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                j = stack.pop()
                ans[j] = nums[i]

            stack.append(i)

        return ans[:n]
            
        