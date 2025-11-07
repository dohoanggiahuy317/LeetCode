class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        mul = 0
        prefix = ""
        for char in s:
            if char.isalpha():
                prefix += char
            
            elif char.isdigit():
                mul = mul * 10 + int(char)
            
            elif char == "[":
                stack.append([mul, prefix])
                mul = 0
                prefix = ""

            elif char == "]":
                prev_mul, prev_prefix = stack.pop()
                prefix = prev_prefix + prefix * prev_mul

        return prefix

            
