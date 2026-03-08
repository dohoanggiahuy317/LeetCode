class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_words = Counter(s1.split(" "))
        s2_words = Counter(s2.split(" "))
        
        uncommon1 = [word for word, freq in s1_words.items() if (word not in s2_words and freq == 1)]
        uncommon2 = [word for word, freq in s2_words.items() if (word not in s1_words and freq == 1)]

        return uncommon1 + uncommon2

        