class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        prefix_area = [0] * n
        left_stack = [-1] # stack of idx that only decreasing

        for i, h in enumerate(heights):
            # pop all for non_decrease
            while len(left_stack) > 1 and heights[left_stack[-1]] >= h:
                left_stack.pop()
            
            # compute the prefix_area
            prefix_area[i] = h * (i - left_stack[-1])
            left_stack.append(i)

        # Calculate suffix area        
        ans = 0
        right_stack = [n]
        for i in range(n - 1, -1, -1):
            h = heights[i]

            while len(right_stack) > 1 and heights[right_stack[-1]] >= h:
                right_stack.pop()

            # use prefix and suffix to get ans
            suffix_area = h * (right_stack[-1] - i)
            ans = max(suffix_area + prefix_area[i] - h, ans)
            
            right_stack.append(i)

        return ans
        