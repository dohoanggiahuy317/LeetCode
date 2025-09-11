class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token[0] == '-' and len(token) > 1:
                stack.append(-int(token[1:]))
            elif token[0].isnumeric():
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                if token == "+":
                    val = num1 + num2
                elif token == "-":
                    val = num1 - num2
                elif token == "*":
                    val = num1 * num2
                else:
                    val = num1 / num2
                    val = int(val) if val >= 0 else math.ceil(val)

                stack.append(val)

        return stack[0]
