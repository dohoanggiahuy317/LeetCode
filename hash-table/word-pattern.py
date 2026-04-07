class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s_li = s.split(" ")
        if len(s_li) != len(pattern):
            return False

        word_patt = {}
        patt_word = {}

        for char, word in zip(pattern, s_li):
            if char in patt_word and patt_word[char] != word:
                return False
            if word in word_patt and word_patt[word] != char:
                return False

            patt_word[char] = word
            word_patt[word] = char

            
        return True