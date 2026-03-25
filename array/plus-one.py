class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        digits.reverse()

        for i, digit in enumerate(digits):
            digits[i] += carry
            if digits[i] >= 10:
                digits[i] %= 10
                carry = 1
            else:
                carry = 0

        if carry == 1:
            digits.append(1)

        digits.reverse()

        return digits