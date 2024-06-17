class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        if c % 8 not in [0, 1, 2, 4, 5]:
            return False
        if c % 4 == 3:
            return False

        temp = [i ** 2 for i in range(int(math.sqrt(c) + 1))]
        s = 0
        e = len(temp) - 1

        while s <= e:
            if temp[s] + temp[e] > c:
                e -= 1
            elif temp[s] + temp[e] < c:
                s += 1
            else:
                return True
        return False
