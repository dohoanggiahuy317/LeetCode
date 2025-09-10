class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        prefix_area = [0] * n
        idx_left_stack = [-1] # stack of idx that only non-decreasing

        for i, h in enumerate(heights):
            # pop all for non_decrease
            while len(idx_left_stack) > 1 and heights[idx_left_stack[-1]] > h:
                idx_left_stack.pop()
            
            # compute the prefix_area
            prefix_area[i] = h * (i - idx_left_stack[-1])
            idx_left_stack.append(i)

        ans = 0
        idx_right_stack = [n]
        for i in range(n - 1, -1, -1):
            h = heights[i]
            while len(idx_right_stack) > 1 and heights[idx_right_stack[-1]] > h:
                idx_right_stack.pop()

            suffix_area = h * (idx_right_stack[-1] - i)
            ans = max(suffix_area + prefix_area[i] - h, ans)
            idx_right_stack.append(i)

        return ans
        