class Solution:
    def revEa(self, x):
        return "".join(list(x)[::-1])

    
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")

        s = list(map(lambda x: self.revEa(x), s))

        return " ".join(s)