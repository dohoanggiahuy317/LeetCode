class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def cast_vowel(word):
            VOWELS = "uoeaiUEOAI"
            ans = ""
            for char in word:    
                ans += char.lower() if char not in VOWELS else "*"

            return ans
        
        set_words = set(wordlist)
        novowel_words = {}
        lower_words = {}

        for word in wordlist:
            if (novowel_word := cast_vowel(word)) not in novowel_words:
                novowel_words[novowel_word] = word
            if (word_lower := word.lower()) not in lower_words:
                lower_words[word_lower] = word

        ans = []
        for q in queries:
            if q in set_words:
                ans.append(q)
            elif (q_lower := q.lower()) in lower_words:
                ans.append(lower_words[q_lower])
            elif (novowel_q := cast_vowel(q)) in novowel_words:
                ans.append(novowel_words[novowel_q])
            else:
                ans.append("")

        return ans