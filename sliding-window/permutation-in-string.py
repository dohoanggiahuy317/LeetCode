class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k, n = len(s1), len(s2)
        s1_c = Counter(s1)
        s2_c = Counter(s2[:k])

        if s2_c == s1_c:
            return True

        for r in range(k, n):

            s2_c[s2[r]] += 1
            s2_c[s2[r - k]] -= 1

            if s1_c == s2_c:
                return True


        return False




