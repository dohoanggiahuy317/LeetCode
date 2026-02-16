class Solution:
    def smallestNumber(self, num: int) -> int:
        digits = list(str(abs(num)))
        digits.sort()

        if num < 0:
            smallest = "".join(digits[::-1])
            return - int(smallest)
        
        for i, num in enumerate(digits):
            if num != "0":
                digits[i], digits[0] = digits[0], digits[1]
                break

        smallest = "".join(digits)
        return int(smallest)

        