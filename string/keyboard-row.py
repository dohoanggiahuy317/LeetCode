class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        set1 = set("qwertyuiop")
        set2 = set("asdfghjkl")
        set3 = set("zxcvbnm")
        sets = [set1, set2, set3]
        ans = []

        for word in words:
            for s in sets:
                if all(char in s for char in word.lower()):
                    ans.append(word)

        return ans