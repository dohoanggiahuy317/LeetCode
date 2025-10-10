class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        word = []

        while i < len(word1) and j < len(word2):
            word.append(word1[i])
            word.append(word2[j])
            i += 1
            j += 1
        # print(i, j, word2[j:], word1[i:])
        if i < len(word1):
            word.append(word1[i:])
        if j < len(word2):
            word.append(word2[j:])

        # print(word)

        return "".join(word)