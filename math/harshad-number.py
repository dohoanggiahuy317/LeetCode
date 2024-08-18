class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        if x % sum(list(map(int, list(str(x))))) == 0:
            return sum(list(map(int, list(str(x)))))
        return -1