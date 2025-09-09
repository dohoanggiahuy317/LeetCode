class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        freq_stack = []
        char_stack = []

        for char in s:

            if char_stack and char == char_stack[-1]:
                freq_stack[-1] += 1
            else:
                char_stack.append(char)
                freq_stack.append(1)

            if freq_stack[-1] == k:
                freq_stack.pop()
                char_stack.pop()

        return "".join([c * f for c, f in zip(char_stack, freq_stack)])
