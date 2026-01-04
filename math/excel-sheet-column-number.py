class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
#         from string import ascii_uppercase
#         my_dict = dict()
        
#         i = 1
#         for j in ascii_uppercase:
#             my_dict[j] = i
#             i += 1
                
#         n = len(columnTitle)
#         res = 0
        
#         for index in range(n):
#             res += my_dict[columnTitle[index]] * (26**(n-index-1))

#         return res

        res = 0
        for char in columnTitle:
            res *= 26
            res += ord(char)-ord('A')+1
        return res