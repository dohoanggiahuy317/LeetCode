class Solution:

    def __init__(self, w: List[int]):
        self.pref = list(accumulate(w))
        self.s = self.pref[-1]

    def pickIndex(self) -> int:
        tar = random.randint(1, self.s)
        l, r = 0, len(self.pref) - 1

        while l < r:
            m = (l + r) // 2
            if self.pref[m] < tar:
                l = m + 1
            elif self.pref[m] > tar:
                r = m
            else:
                return m

        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()