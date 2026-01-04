class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        val = 0
        for i in range(len(digits)):
            val += digits[i] * (10 ** (n - 1 - i))
        val += 1
        tempt = list(str(val))

        res = []
        for i in tempt:
            res.append(int(i)) 
        return res