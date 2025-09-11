class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            # print(token, stack)
            if token.startswith('-') and token[1:].isnumeric():
                stack.append(-int(token[1:]))
            elif token.isnumeric():
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                val = -1

                if token == "+":
                    val = num1 + num2
                if token == "-":
                    val = num1 - num2
                if token == "*":
                    val = num1 * num2
                if token == "/":
                    val = num1 // num2 if num1 * num2 >= 0 else math.ceil(num1 / num2)

                stack.append(val)

        return stack[0]
