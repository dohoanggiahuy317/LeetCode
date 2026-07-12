class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        primitive = []
        ans = []

        for char in s:
            primitive.append(char)
            if char == "(":
                stack.append(char)
            else:
                stack.pop()

            if not stack:
                ans.append("".join(primitive[1:-1]))
                primitive = []

        return "".join(ans)