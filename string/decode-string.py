class Solution:
    def decodeString(self, s: str) -> str:

        prefix, freq = "", 0
        stack = []

        for char in s:
            if char.isdigit():
                freq = freq * 10 + int(char)
            elif char == "[":
                stack.append((prefix, freq))
                freq = 0
                prefix = ""
            elif char == "]":
                prev_prefix, prev_freq = stack.pop()
                prefix = prev_prefix + prev_freq * prefix
            else:
                prefix += char

        return prefix

            
