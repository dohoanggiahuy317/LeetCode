class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for x in details:
            if int(x[11:13]) > 60:
                count += 1
        return count