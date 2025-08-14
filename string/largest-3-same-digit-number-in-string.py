class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        temp = -1
        for i in range(len(num) - 3):
            if len(set(list(num[i: i + 3]))) == 1:
                if int(num[i: i + 3]) > temp:
                    ans = num[i: i + 3]
                    temp = int(num[i: i + 3])

        return ans