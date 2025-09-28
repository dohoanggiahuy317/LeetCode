class Solution:
    def longestDupSubstring(self, s: str) -> str:
        seen = {""}
        endings = {""}
        ans = ""

        for ch in s:
            new_endings = {sub + ch for sub in endings} | {""}

            for t in new_endings:
                if t in seen and len(t) > len(ans):
                    ans = t

            seen |= new_endings
            endings = new_endings | {""}

        return ans