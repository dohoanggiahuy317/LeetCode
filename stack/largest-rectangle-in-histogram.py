class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        prev_smallest = [-1] * n
        next_smallest = [n] * n
        stack = []

        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                next_smallest[stack.pop()] = i

            if stack:
                prev_smallest[i] = stack[-1]
            stack.append(i)

        return max([(r - l - 1) * h for l, r, h in zip(prev_smallest, next_smallest, heights)])

        