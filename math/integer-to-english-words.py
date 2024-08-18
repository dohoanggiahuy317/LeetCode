class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
                "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(n):
            if n == 0:
                return []
            elif n < 20:
                return [ones[n]]
            elif n < 100:
                return [tens[n // 10]] + helper(n % 10)
            else:
                return [ones[n // 100], "Hundred"] + helper(n % 100)

        words = []
        for i in range(len(thousands)):
            if num % 1000 != 0:
                words = helper(num % 1000) + ([thousands[i]] if i > 0 else []) + words
            num //= 1000

        return " ".join(words).strip()