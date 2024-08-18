class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        temp = [i for i in range(1, n+1)]
        temp += temp[::-1][1:n-1]
        # print(temp)

        return temp[time%len(temp)]