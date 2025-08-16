class Solution:
    def maximum69Number (self, num: int) -> int:
        for i, ch in enumerate(str(num)):
            if ch == "6":
                return int(str(num)[:i] + "9" + str(num)[i+1:])
        return num