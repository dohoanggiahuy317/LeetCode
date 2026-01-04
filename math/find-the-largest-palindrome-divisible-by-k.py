class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        def create_palindrome(left_half: str, odd_length: bool) -> int:
            if odd_length:
                return int(left_half + left_half[-2::-1])
            else:
                return int(left_half + left_half[::-1])
    
        half_length = (n + 1) // 2
        largest_half = "9" * half_length

        
        if k == 1:
            return "9" * n
        
        if k == 2:
            if n == 1:
                return "8"
            return "8" + "9" * (n-2) + "8"
        
        if k in [3, 9]:
            return "9" * n
        
        if k == 4:
            if n == 1:
                return '8'
            elif n == 2:
                return '88'
            elif n == 3:
                return '888'
            else:
                return '88' + '9' * (n - 4) + '88'
        
        if k == 5:
            if n == 1:
                return "5"
            return "5" + "9" * (n - 2) + "5"

        
        if k == 6:
            if n < 3:
                return "6" * n

            if n % 2 == 1:
                return "8" + "9" * (half_length - 2) + "8" +  "9" * (half_length - 2) + "8"
            if n >= 6:
                return "8" + "9" * (half_length - 2) + "77" + "9" * (half_length - 2) + "8"
            if n == 4:
                return "8778"
        
        if k == 7:
            d = [
                "7",
                "77",
                "959",
                "9779",
                "99799",
                "999999",
                "9994999",
                "99944999",
                "999969999",
                "9999449999",
                "99999499999"
            ]
            if n < 12:
                return d[n-1]
            if n == 12:
                return "999999999999"
            s = n % 12
            t = n//12
            
            if s == 0:
                return "999999" * t + "999999" * t

            return "999999" * t + d[s-1] + "999999" * t
            

        if k == 8:
            if n >= 6:
                return "888" + "9" * (n-6) + "888"
            return "8" * n
           
        return ""


        # # Helper function to check if a number is a palindrome
        # def is_palindrome(x: int) -> bool:
        #     s = str(x)
        #     return s == s[::-1]
        
        # # Start with the largest n-digit number
        # max_num = 10**n - 1
        
        # # Generate the largest possible palindromes and check for divisibility
        # for num in range(max_num, 10**(n-1) - 1, -1):
        #     if is_palindrome(num) and num % k == 0:
        #         return str(num)
        
        # return ""