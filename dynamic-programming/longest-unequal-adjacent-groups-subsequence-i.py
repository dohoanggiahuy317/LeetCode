class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        border = []

        for i in range(len(groups)):
            if  border == [] or groups[i] != groups[i-1]:
                border.append(words[i])
            else:
                continue

        return border

        
