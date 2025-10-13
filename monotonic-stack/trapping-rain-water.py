class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        stack = []
        ans = 0

        for i, this_height in enumerate(height):
            while stack and height[stack[-1]] < this_height:
                top = stack.pop()
            
                if not stack:
                    break
                    
                dist = i - stack[-1] - 1
                h = min(this_height, height[stack[-1]]) - height[top]

                ans += dist * h
                
            stack.append(i)

        return ans
                
