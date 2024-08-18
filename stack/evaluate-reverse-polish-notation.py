class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l = []
        s = set(["+", "-", "*", "/"])

        for x in tokens:
            # print(l)
            if x not in s:
                l.append(int(x))
            else:
                x1 = l.pop(len(l) - 1)
                x2 = l.pop(len(l) - 1)

                if x == "+":
                    l.append(x1 + x2)
                if x == "-":
                    l.append(x2 - x1)
                if x == "*":
                    l.append(x1 * x2)
                if x == "/":
                    l.append(int(x2/x1))

        return l[0]