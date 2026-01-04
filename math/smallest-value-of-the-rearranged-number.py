class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        
        if num > 0:
            all_digits = list(str(num))
            digit_non_zero = []
            zeros = 0
            res = ""

            for digit in all_digits:
                if digit != "0":
                    digit_non_zero.append(int(digit))
                else:
                    zeros += 1

            digit_non_zero.sort()

            res += str(digit_non_zero[0]) 

            if zeros != 0:
                res += "0" * zeros

            if len(digit_non_zero) > 1: 
                for digit in digit_non_zero[1:]:
                    res += str(digit)

            return int(res)
        
        if num < 0:
            all_digits = list(str(num)[1:])
            digit_non_zero = []
            zeros = 0
            res = ""

            for digit in all_digits:
                if digit != "0":
                    digit_non_zero.append(int(digit))
                else:
                    zeros += 1

            digit_non_zero.sort(reverse = True)

            res += str(digit_non_zero[0]) 


            if len(digit_non_zero) > 1: 
                for digit in digit_non_zero[1:]:
                    res += str(digit)
            
            if zeros != 0:
                res += "0" * zeros

            return int("-"+res)
        