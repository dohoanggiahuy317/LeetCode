class Solution:
    def isValid(self, s: str) -> bool:
        paren = {"[": "]", "(": ")", "{": "}",}
        stack = []

        for char in s:
            if char in "[({":
                stack.append(char)
            else:
                if not (stack and paren[stack[-1]] == char):
                    return False
                stack.pop()

        return True
