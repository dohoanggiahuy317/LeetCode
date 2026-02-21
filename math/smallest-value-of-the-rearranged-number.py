class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            non_zero = [x for x in str(num) if x != '0']
            sorted_digit = sorted(non_zero)
            
            n = len(str(num))
            rounded_leading_digit = int(sorted_digit[0]) * (10 ** (n - 1))
            no_leading_digit = int(''.join(sorted_digit[1:])) if len(sorted_digit) > 1 else 0

            return rounded_leading_digit + no_leading_digit
               
        num = abs(num)
        sorted_digit = sorted(str(num), reverse = True)
        smallest = ''.join(str(x) for x in sorted_digit)
        return -int(smallest)

