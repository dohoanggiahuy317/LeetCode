class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()

        for x in emails:
            p1, p2 = x.split("@")

            p1 = "".join(p1.split("."))
            p1 = p1.split("+")[0]

            s.add((p1, p2))

        return len(s)

        