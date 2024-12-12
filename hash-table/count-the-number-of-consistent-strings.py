class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        s = set(list(allowed))
        ans = 0

        for word in words:
            c = True
            for char in list(word):
                if char not in s:
                    c = False
                    break

            if c:
                ans += 1

        return ans
            


