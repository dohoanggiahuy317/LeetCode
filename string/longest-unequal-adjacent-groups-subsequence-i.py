class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        if len(groups) == 1:
            return words
            
        border = []

        for i in range(1, len(groups)):
            if words[i] == words[i-1]:
                continue
            else:
                border.append(words[i])

        return border

        
