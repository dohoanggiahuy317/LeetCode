class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        als = set(list(allowed))
        ans = 0
        for word in words:
            b = True
            for char in list(word):
                if char not in als:
                    b = False
                    break

            if b:
                ans += 1

        return ans