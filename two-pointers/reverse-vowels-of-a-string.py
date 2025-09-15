class Solution:
    def reverseVowels(self, s: str) -> str:
        
        char_list, idx_list = [], []
        for i, char in enumerate(s):
            if char in "ueoaiUEOAI":
                char_list.append(char)
                idx_list.append(i)

        vowel_map = dict(zip(idx_list, char_list[::-1]))

        ans
        for i, char in enumerate(s):
            if i not in vowel_map:
                ans += char
            else:
                ans += vowel_map[i]

        return ans