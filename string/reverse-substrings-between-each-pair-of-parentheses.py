class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == '(':
                stack.append("(")
            elif char == ')':
                rev = []
                while stack and stack[-1] != "(":
                    rev.append(stack.pop()[::-1])
                stack.pop() # Remove the '('
                stack.append("".join(rev))
            else:
                stack.append(char)
        
        return "".join(stack)