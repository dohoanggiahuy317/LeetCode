class Solution:

    def __init__(self, w: List[int]):
        self.pref = [0] * (len(w) + 1)
        for i, num in enumerate(w):
            self.pref[i + 1] = self.pref[i] + num
        self.pref = self.pref[1:]
        self.s = sum(w)

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