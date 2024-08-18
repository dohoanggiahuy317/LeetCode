class Solution:
    def makeGood(self, s: str) -> str:
        def is_bad(a, b):
            delta = ord('a') - ord('A')
            return abs(ord(a) - ord(b)) == delta
            
        picked = []
        for char in s:
            if picked and is_bad(picked[-1], char):
                picked.pop()
            else:
                picked.append(char)
        return ''.join(picked)

