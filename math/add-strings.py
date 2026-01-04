class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        le = max(len(num1), len(num2))

        num1 = "0"*(le-len(num1)) + num1
        num2 = "0"*(le-len(num2)) + num2

        rem = 0

        for i in range(len(num1)-1, -1, -1):
            su = str(int(num1[i]) + int(num2[i]) + rem)

            res = su[-1] + res
            rem = int(su[0]) if len(su) > 1 else 0
        if rem > 0:
            res = str(rem) + res 

        return res