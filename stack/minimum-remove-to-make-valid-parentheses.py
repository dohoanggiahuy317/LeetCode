class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_paren = 0
        chars = []

        for char in s:
            if char == "(":
                open_paren += 1
                chars.append(char)
            elif char == ")":
                open_paren -= 1
                if open_paren < 0:
                    open_paren = 0
                else:
                    chars.append(char)
            else:
                chars.append(char)

        ans = []
        for i in range(len(chars) - 1, -1, -1):
            if open_paren > 0 and chars[i] == "(":
                open_paren -= 1
            else:
                ans.append(chars[i])
        

        return "".join(ans[::-1])