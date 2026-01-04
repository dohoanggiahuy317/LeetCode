class Solution:
    def countSegments(self, s: str) -> int:
        sp = s.split(" ")
        count = 0
        for x in sp:
            count += 1 if x != "" else 0
        return count