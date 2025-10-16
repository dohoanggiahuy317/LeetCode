class Solution:
    def removeSubstring(self, s: str, k: int) -> str:

        stack = []
        for char in s:
            if stack and char == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])

            if len(stack) >= 2 and stack[-1][0] == ")" and stack[-1][1] == k and stack[-2][1] >= k:
                closes = stack.pop()
                opens = stack.pop()
                opens[1] = opens[1] - k

                if opens[1] > 0:
                    open_count = opens[1]
                    stack.append(["(", open_count])
                
                # if open_counts[-1] == k:
                #     open_counts.pop()
                # else:
                #     open_counts[-1] = open_counts[-1] - k
                
                # if stack and open_counts and stack[-1] == "(":
                #     open_count = open_counts.pop(-1)
        ans = ""
        for x, y in stack:
            ans += x * y
        return ans
                

            