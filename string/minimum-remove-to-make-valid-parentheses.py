class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = []
        open_paren = 0

        for char in s:
            if char == "(":
                ans.append(char)
                open_paren += 1
            elif char == ")":
                if open_paren == 0:
                    continue
                else:
                    open_paren -= 1
                    ans.append(char)
            else:
                ans.append(char)
        
        temp = ans[::-1]
        ans = []
        close_paren = 0

        for char in temp:
            if char == ")":
                ans.append(char)
                close_paren += 1
            elif char == "(":
                if close_paren == 0:
                    continue
                else:
                    close_paren -= 1
                    ans.append(char)
            else:
                ans.append(char)

        return "" .join(ans[::-1])