class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0

        for x in s:
            if x == "1":
                count += 1

        if count == 1:
            return "0" * (len(s) - 1) + "1"
        else:
            return (count - 1) * "1" + (len(s) - count) * "0" + "1"