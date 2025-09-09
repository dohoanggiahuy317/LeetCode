class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        stack = []
        ans = [0] * n

        for i, t in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]] < t:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            
            stack.append(i)

        return ans
                
                
            
