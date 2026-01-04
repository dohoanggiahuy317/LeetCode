class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        DNA_MAP = {"A": 3, "C": 2, "G": 1, "T": 0}
        MASK = 4 ** 9 # Can use binary lifting for optimize here (?)

        seq = 0
        for char in s[:10]:
            seq = seq * 4 + DNA_MAP[char]

        visited, ans = set([seq]), set()

        for r in range(10, len(s)):
            l = r - 9

            seq = (seq - DNA_MAP[s[l - 1]] * MASK) * 4 + DNA_MAP[s[r]]
            if seq in visited:
                ans.add(s[l: r + 1])
            visited.add(seq)

        return list(ans)