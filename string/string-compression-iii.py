class Solution:
    def compressedString(self, word: str) -> str:
        if len(word) == 1:
            return str(1) + word
        s = 0
        comp = ""
        last = 0
        
        while s < len(word):
            prev = s
            while s < len(word) - 1 and word[s] == word[s + 1] and s-prev < 8:
                s += 1
            
            comp += str(s-prev + 1) + word[s]
            s += 1
            
            
        
#         if word[-1] != word[-2]:
#             comp += str(1) + word[-1]
            
        
        
        return comp