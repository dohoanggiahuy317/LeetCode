class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return "-".join(list(map(lambda x: bin(int(x))[2:], date.split("-"))))
