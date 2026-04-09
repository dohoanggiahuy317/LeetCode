class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        li_s = list(s)
        last_open = len(s) - 1
        count = 0

        for i, bracket in enumerate(li_s):
            if bracket == "[":
                stack.append(bracket)
            elif stack:
                stack.pop()
            else:
                while li_s[last_open] != "[":
                    last_open -= 1

                count += 1
                li_s[i], li_s[last_open] = li_s[last_open], li_s[i]
                stack.append(bracket)

        return count

                