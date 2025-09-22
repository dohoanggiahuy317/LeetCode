class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        curr_word = words[0]
        curr_counter = Counter(curr_word)

        for word in words + [""]:
            word_counter = Counter(word)
            if word_counter != curr_counter:
                ans.append(curr_word)
                curr_word = word
                curr_counter = word_counter

        return ans