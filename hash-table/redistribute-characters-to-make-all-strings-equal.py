class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = {}

        for word in words:
            for char in word:
                if char not in d:
                    d[char] = 1
                else:
                    d[char] += 1
                    
        for char, appr in d.items():
            if appr % len(words) != 0:
                return False

        return True