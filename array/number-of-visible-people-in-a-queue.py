class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        ans = [1] * len(heights)

        for i, h in enumerate(heights):
            count = 1

            while stack and stack[-1][1] < h:
                cur_i, cur_h = stack.pop()
            
                if stack:
                    ans[stack[-1][0]] += 1

            stack.append((i, h))

        for idx, (i, h) in enumerate(stack):
            ans[i] = len(stack) - idx - 1

        return ans