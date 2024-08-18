class Solution:
    def getSmallestString(self, s: str) -> str:
        num = []

        i = 0
        swap = False
        while i  < len(s) - 1:
            if (int(s[i]) - int(s[i + 1])) % 2 == 0 and not swap:
                if int(s[i]) > int(s[i + 1]):
                    num.append(s[i+1])
                    num.append(s[i])
                    i += 2
                    swap = True
                else:
                    num.append(s[i])
                    i += 1
            else:
                num.append(s[i])
                i += 1

        if len(num) < len(s):
            num.append(s[-1])
        return "".join(num)