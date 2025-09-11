class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                num2 = stack.pop()
                num1 = stack.pop()
                val = num1 + num2
            elif token == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                val = num1 - num2
            elif token == "*":
                num2 = stack.pop()
                num1 = stack.pop()
                val = num1 * num2
            elif token == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                val = num1 / num2
                val = int(val) if val >= 0 else math.ceil(val)
            else:
                val = int(token)
            
            stack.append(val)

        return stack[0]
