class Solution:
    def romanToInt(self, s: str) -> int:
        di = {  'I': 1, 
                'V': 5, 
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000}

        count = 0

        for i in range(len(s) - 1):
            if di[ s[i] ] < di[ s[i+1] ]:
                count -= di[ s[i] ]
            else:
                count += di[ s[i] ]

        count += di[ s[ len(s)-1 ] ]

        return count