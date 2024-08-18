class Solution:
    def isValid(self, s: str) -> bool:
        q = []

        for x in s:
            if x in "([{":
                q.append(x)
            elif x == ")" and len(q) > 0 and q[-1] == "(":
               q.pop(-1)
            elif x == "}" and len(q) > 0 and q[-1] == "{":
               q.pop(-1)
            elif x == "]" and len(q) > 0 and q[-1] == "[":
               q.pop(-1)
            else:
                # print(q)
                return False

        return q == []

