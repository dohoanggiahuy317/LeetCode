class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])

        for word in words[1:]:
            word_counter = Counter(word)

            for char, freq in common.items():
                if char not in word_counter:
                    common[char] = 0
                else:
                    common[char] = min(word_counter[char], freq)
            
        return list(common.elements())