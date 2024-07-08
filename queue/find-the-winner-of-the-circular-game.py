class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        l = [i for i in range(1, n+1)]
        start = 0

        while len(l) > 1:
            ind = (start + k - 1) % len(l)
            l.pop(ind)
            start = ind

        return l[0]